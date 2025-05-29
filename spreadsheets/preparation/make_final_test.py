import json
import pandas as pd

with open('analysis/idioms_map.json', 'r', encoding='utf-8') as f:
    idioms_map = json.load(f)

res = [(idiom_id, 
        f'Вам знакомо выражение "{idioms_map[idiom_id]["idiom"]}" в значении "{idioms_map[idiom_id]["meaning"]}"')
        for idiom_id in idioms_map]

res = pd.DataFrame(res, columns=['idiom_question_id', 'idiom_question'])
res.to_excel('spreadsheets/idiom_test.xlsx', index=False)
