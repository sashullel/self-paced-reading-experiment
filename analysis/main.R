install.packages(c("lme4", "lmerTest", "pbkrtest", "sjPlot", "sjmisc", "knitr", "kableExtra", "interactions", "ggplot2", "correlation"))
library(dplyr)
library(emmeans)  # for post-hoc tests
library(ggplot2)
library(lme4)
library(lmerTest) # for p-values
library(sjPlot)
library(webshot)
library(sjmisc)
library(knitr)
library(correlation) 
library(kableExtra)


# -------------------------- loading, processing & examining data


data <- read.csv('analysis/data/three_df.csv')
names(data)

data <- data %>%
  mutate(
    # categorical nominal feature (no inherent order)
    sent_type = factor(type, levels = 1:4, ordered = FALSE),
    # ordered factor
    trial_order = factor(trial_order, ordered = TRUE),
    # categorical participant IDs
    participant = factor(participant),
    # contrast-coded binary predictors (kept as numeric for modeling)
    biasing_context = as.numeric(biasing_context),
    resolution_type = as.numeric(resolution_type), 
    # keep the continuous predictors as numeric (already scaled)
    across(c(ipm, ipm_bri, frequency, familiarity, literality), as.numeric),
    # keep RT variable as numeric
    unit_rt_log = as.numeric(unit_rt_log)
  )

glimpse(data)
levels(data$sent_type)

cor_matrix <- data %>% 
  select(ipm, ipm_bri, frequency, familiarity, literality) %>%
  correlation()
cor_matrix

# --------------------------


# -------------------------- base model for examining random effects

full_base_model <- lmer(unit_rt_log ~ 1 + (1 | participant) + (1 | trial_order),
                        data = data)

# LRT with ranova
ranova_results <- ranova(full_base_model)
ranova_results

# make a table
results_df <- as.data.frame(ranova_results) |>
  tibble::rownames_to_column("Effect") |>
  mutate(
    p_value = ifelse(is.na(`Pr(>Chisq)`),
                     NA_character_,
                     ifelse(`Pr(>Chisq)` < 0.001,
                            "<0.001",
                            format(round(`Pr(>Chisq)`, 3), nsmall = 3)))
  ) |>
  select(Effect, npar, logLik, AIC, LRT, Df, p_value)

# save table as HTML
tab_df(results_df,
       title = "Random Effects ANOVA Results",
       file = "analysis/results/random_effects_five.html",
       show.rownames = FALSE,
       alternate.rows = TRUE)

# --------------------------

# -------------------------- avoid multicollinearity

frequency_familiarity <- c("frequency", "familiarity")
ipm_ipm_bri <- c("ipm", "ipm_bri")
combinations <- expand.grid(frequency_familiarity, ipm_ipm_bri)

model_results <- list()

# build model for every combination of predictors
for (i in 1:nrow(combinations)) {
  freq_fam <- combinations[i, 1]
  ipm_type <- combinations[i, 2]
  
  formula <- as.formula(paste("unit_rt_log ~ literality +", ipm_type, "+", freq_fam, "+ biasing_context + (1 | participant) + (1 | trial_order)"))
  model <- lmer(formula, data = data, REML = TRUE)
  model_results[[paste(freq_fam, ipm_type, sep = "_")]] <- list(model = model, aic = AIC(model))
}
results_df <- data.frame(
  Model = names(model_results),
  AIC = sapply(model_results, function(x) x$aic)
)

results_df <- results_df %>% arrange(AIC)

print(results_df)

best_model_name <- results_df$Model[1]
best_model <- model_results[[best_model_name]]$model
cat('best model:', best_model_name, "\n")

# -------------------------- result - include ipm + familiarity

# -------------------------- mixed-effects model

# for idiom segment
model <- lmer(unit_rt_log ~ literality * (ipm + familiarity + biasing_context) + 
                (1 | participant) + (1 | trial_order),
              data = data)

# for resolution and last segment
# model <- lmer(unit_rt_log ~ literality * (ipm + familiarity + biasing_context * resolution_type) + 
#                 (1 | participant) + (1 | trial_order),
#               data = data)

# Get model summary
summary(model)

tab_model(
  model,
  show.ci = TRUE,
  show.se = TRUE,
  show.stat = TRUE,
  show.df = TRUE,
  show.p = TRUE,
  p.style = "stars",
  digits = 5,
  title = "Mixed-Effects Model Results for Reading Times",
  file = "analysis/results/idiom_segment/model_results.html"
)
