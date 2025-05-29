# This is a self-paced reading task for online study of idiom processing

---- 

## Getting started
The stimuli is created using a Python script `spreadsheets/make_spreadsheets.py`. 

To run this script, you would first need to:

1. Place rough stimulus materials in the `spreadsheet/preparation/` directory considering the following:
- Use ```my_sentences.txt``` as the input file name (or change the input file path in the `make_spreadsheets.py`)

- Each line of the .txt file must consist of the following parts, separated by semicolon (`;`)

     - sentence
     - question

     - correct answer (y/n)
     - type of the sentence (0/1/2/3/4)
     - idiom id
     - group number


2. Run `make_spreadsheets.py` and make sure that the necessary files have been created in the directory.

3. Run `self_pased_readings.psyexp`


```
python spreadsheets\test\make_test_spreadsheets.py
python spreadsheets\preparation\make_spreadsheets.py
python spreadsheets\preparation\make_final_test.py
```

---

## Analyzing results
You can find the reaction times for each segment in the column ```key_resp.rt```. 



Check the ```analysis``` directory for analysis script.
