import pandas as pd


def read_file(input_path: str) -> tuple[list]:
    """
    Reads a .txt file containing stimulus materials

    Args:
        input_path (str): Path to the .txt file where each line is of the format: text;question;answer;type;idiom_id;group
    Returns:
        tuple: Tuple with lists of texts, questions, groups
    """
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = [line.strip().split(';') for line in f.readlines() if line.strip() and not line.startswith('#')] 
    
    texts, questions, answers, types, idiom_ids, groups = [], [], [], [], [], []
    for line in lines:
        try:
            texts.append(line[0])
            questions.append(line[1])
            answers.append(line[2])
            types.append(int(line[3]))
            idiom_ids.append(int(line[4]))
            groups.append(int(line[5]))
        
        except IndexError:
            print(line)
            raise IndexError

    return texts, questions, answers, types, idiom_ids, groups


def mask_text(text: str) -> list[str]:
    """
    Masks given string with underscores by fragments

    Args:
        text (str): Sentence separated with '/' into fragments
    Returns:
        list: List of masked texts for each fragment of the sentence
    """
    no_underline_symbols = ' .,!?\'\"'    
    masked = []
    
    fragments = text.split('/')
    for i, fragment in enumerate(fragments):
        masked_string = ''
        
        for j, f in enumerate(fragments):
            if j != i: # if not the current fragment
                masked_string += ' ' + ''.join(['_' if c not in no_underline_symbols else c for c in f])
            else:
                masked_string += fragment
        masked.append(masked_string)

    return masked


def save_stimuli(texts: list[str], questions: list[str], answers: list[str],
                 types: list[int], idiom_ids: list[str], groups: list[int], output_path: str) -> None:
    """
    Saves stimuli into separate .csv files by group

    Args:
        texts (list): List of stimulus sentences
        questions (list): List of the questions followign the stimulus sentences
        answers (list): List of answers (y/n) to the questions
        types (list): List of stimulus sentences types
        idiom_ids (list): List of idioms ids in the stimulus sentences
        groups (list): List of groups for distributing stimuli
        output_path (str): Directory path for saving stimulus passages by groups
    """
    group1_paths = []
    group2_paths = []

    for i in range(len(texts)):

        final_output_path = f'{output_path}/group_{groups[i]}/passage_{i}.csv'
        if groups[i] == 1:
            group1_paths.append(final_output_path)
        else:
            group2_paths.append(final_output_path)

        masked_text = mask_text(texts[i])
        sheet = {
            'sent_id': i,
            'sent_text': texts[i],
            'masked_segment': masked_text,
            'segment_id': [i for i in range(1, len(masked_text) + 1)],
            'question_text': questions[i],
            'answer': answers[i],
            'type': types[i],
            'idiom_id': idiom_ids[i],
            'group': groups[i]
        }
        pd.DataFrame(sheet).to_csv(final_output_path, encoding='utf-8', index=False)

    pd.DataFrame(group1_paths, columns=['this_file']).to_excel(f'{output_path}/group1_paths.xlsx', index=False)
    pd.DataFrame(group2_paths, columns=['this_file']).to_excel(f'{output_path}/group2_paths.xlsx', index=False)


input_path = 'spreadsheets/preparation/my_sentences.txt'
output_path = 'spreadsheets'
texts, questions, answers, types, idiom_ids, groups = read_file(input_path)
save_stimuli(texts, questions, answers, types, idiom_ids, groups, output_path)
