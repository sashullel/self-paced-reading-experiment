import pandas as pd


def read_file(input_path: str) -> tuple[list]:
    """
    Reads a .txt file containing stimulus materials

    Args:
        input_path (str): Path to the .txt file where each line is of the format: text;question
    Returns:
        tuple: Tuple with lists of texts, questions, groups
    """
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = [line.strip().split(';') for line in f.readlines() if line.strip() and not line.startswith('#')] 

    texts = [line[0] for line in lines]
    questions = [line[1] for line in lines]


    return texts, questions


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


def save_stimuli(texts: list[str], questions: list[str], output_path: str) -> None:
    """
    Save stimuli into separate .csv files by group

    Args:
        texts (list): List of stimulus sentences
        questions (list): List of the questions followign the stimulus sentences
    """
    test_paths = []
    for i in range(len(texts)):

        final_output_path = f'{output_path}/test/passage_{i}.csv'

        masked_text = mask_text(texts[i])
        sheet = {
            'sent_id': i,
            'sent_text': texts[i],
            'masked_segment': masked_text,
            'segment_id': [i for i in range(1, len(masked_text) + 1)],
            'question_text': questions[i]
        }
        pd.DataFrame(sheet).to_csv(final_output_path, encoding='utf-8', index=False)
        test_paths.append(final_output_path)

    pd.DataFrame(test_paths, columns=['file_path']).to_excel(f'{output_path}/test/test_paths.xlsx', index=False)


input_path = 'spreadsheets/test/test_sentences.txt'
output_path = 'spreadsheets'
texts, questions = read_file(input_path)
save_stimuli(texts, questions, output_path)
