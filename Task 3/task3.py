# Making a forward index.
# Now the catch here is that, previously I was implementing it in the Task 2 code, But I am dumb and started the project after a very long time so that code is haunting me without
# any comments. Now I am doing a bad approach of implementing it after the lexicon.
# It decreases the efficiency. Way too much. 😭😭😭😭😭

import os
import json
import re
from nltk import word_tokenize

FOLDER_PATH = r'D:\\Sem Projects\\DSA Project\\General Shit\\practise\\dir'

filenames = os.listdir(FOLDER_PATH)

forward_index = {}

doc_id = 0

lex_file = open(f'D:\\Sem Projects\\DSA Project\\General Shit\\practise\\Task 3\\lexicon.json')
lex_data = json.load(lex_file)

for i in range(len(filenames)):
    json_file = open(f'D:\\Sem Projects\\DSA Project\\General Shit\\practise\\dir\\{filenames[i]}', 'r')

    data = json.load(json_file)

    for dic in data:
        sent_title = dic['title'].lower()
        sent_content = dic['content'].lower()
        tokenize_title = word_tokenize(sent_title)
        tokenize_content = word_tokenize(sent_content)
        tokenize_title = [i for i in tokenize_title if re.sub(r'[^\w\s]', "", i)]
        tokenize_content = [i for i in tokenize_title if re.sub(r'[^\w\s]', "", i)]

        doc_key = {f'{doc_id}': []}

        for i in range(len(tokenize_title)):
            # if lex_data[f'{tokenize_title[i]}'] not in doc_key:
                if tokenize_title[i] in lex_data.keys():
                    doc_key[f'{doc_id}'].append(lex_data[f'{tokenize_title[i]}'])

        for i in range(len(tokenize_content)):
            # if lex_data[f'{tokenize_content[i]}'] not in doc_key:
                if tokenize_content[i] in lex_data.keys():
                    doc_key[f'{doc_id}'].append(lex_data[f'{tokenize_content[i]}'])

        doc_id += 1
        forward_index.update(doc_key)

    json_file.close()

lex_file.close()

with open('forwardIndex.json', 'w') as outfile:
    json.dump(forward_index, outfile)