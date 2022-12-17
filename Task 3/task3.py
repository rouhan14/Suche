# Making a forward index.
# Now the catch here is that, previously I was implementing it in the Task 2 code, But I am dumb and started the project after a very long time so that code is haunting me without
# any comments. Now I am doing a bad approach of implementing it after the lexicon.
# It decreases the efficiency. Way too much. 😭😭😭😭😭


# Make a doc_key which contains all the keys of the words that exist in the document (==== First if statement ====)
# Then increase the hits (==== Second if statement ====)
# Implementing position too. New scheme: docID: {wordID: {pos: [], hits: integer}}

# ==================== Point to ponder upon: --> Do we really need the position of title. It is just damaging the logic of the code. ====================


import os
import json
import re
from nltk import word_tokenize
from nltk.corpus import stopwords

FOLDER_PATH = r'D:\\Sem Projects\\DSA Project\\General Shit\\practise\\dir'

filenames = os.listdir(FOLDER_PATH)

stop_words = set(stopwords.words('english'))

# Later converted to forwardIndex.json
forward_index = {}

doc_id = 0


def wordID_maker(hit, str):
    wordID = {'pos': [], 'hits': hit, 'type': str}
    return wordID

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
        tokenize_content = [i for i in tokenize_content if re.sub(r'[^\w\s]', "", i)]


        tokenize_title_less_stop_words = []
        tokenize_content_less_stop_words = []

        # Removing stop words from the lists
        for word in tokenize_title:
            if word not in stop_words:
                tokenize_title_less_stop_words.append(word)

        for word in tokenize_content:
            if word not in stop_words:
                tokenize_content_less_stop_words.append(word)

        doc_key = {f'{doc_id}': {}}        


        # Looping for document title
        for i in range(len(tokenize_title_less_stop_words)):
            # Checking if the word in title list exists in the dictionary or not. If it does not then it is updated.
            if tokenize_title_less_stop_words[i] in lex_data.keys() and str(lex_data[f'{tokenize_title_less_stop_words[i]}']) not in doc_key[f'{doc_id}'].keys():   # lex_data has {"word": wordID}
                doc_key[f'{doc_id}'].update({str(lex_data[f'{tokenize_title_less_stop_words[i]}']): wordID_maker(0, 'title')})

            # Checking if the word in title list exists in the dictionary or not. If it does then it is incremented.
            if str(lex_data[f'{tokenize_title_less_stop_words[i]}']) in doc_key[f'{doc_id}'].keys():
                temp = str(lex_data[f'{tokenize_title_less_stop_words[i]}'])
                val = doc_key[f'{doc_id}'][str(temp)]['hits'] + 1
                doc_key[f'{doc_id}'][str(temp)]['hits'] = val

            # incrementing the position list now
            temp2 = str(lex_data[f'{tokenize_title_less_stop_words[i]}'])
            if str(lex_data[f'{tokenize_title_less_stop_words[i]}']) in doc_key[f'{doc_id}'].keys() and doc_key[f'{doc_id}'][str(temp2)]['type'] == 'title': # Not doing it for both a would create contradictions
                doc_key[f'{doc_id}'][str(temp)]['pos'].append(i)

        # Looping for document content
        for i in range(len(tokenize_content_less_stop_words)):
            if tokenize_content_less_stop_words[i] in lex_data.keys() and str(lex_data[f'{tokenize_content_less_stop_words[i]}']) in doc_key[f'{doc_id}'].keys() and doc_key[f'{doc_id}'][str(temp)]['type'] == 'title':
                doc_key[f'{doc_id}'][str(temp)]['type'] = 'both'


            # Checking if the word in content list exists in the dictionary or not. If it does not then it is updated.
            if tokenize_content_less_stop_words[i] in lex_data.keys() and str(lex_data[f'{tokenize_content_less_stop_words[i]}']) not in doc_key[f'{doc_id}'].keys():   # lex_data has {"word": wordID}
                doc_key[f'{doc_id}'].update({str(lex_data[f'{tokenize_content_less_stop_words[i]}']): wordID_maker(0, 'content')})

            # Checking if the word in content list exists in the dictionary or not. If it does then it is incremented
            if str(lex_data[f'{tokenize_content_less_stop_words[i]}']) in doc_key[f'{doc_id}'].keys():
                temp = str(lex_data[f'{tokenize_content_less_stop_words[i]}'])
                val = doc_key[f'{doc_id}'][str(temp)]['hits'] + 1
                doc_key[f'{doc_id}'][str(temp)]['hits'] = val
            
            # incrementing the position list now
            temp2 = str(lex_data[f'{tokenize_content_less_stop_words[i]}'])
            if str(lex_data[f'{tokenize_content_less_stop_words[i]}']) in doc_key[f'{doc_id}'].keys() and doc_key[f'{doc_id}'][str(temp2)]['type'] == 'content' or 'both':
                doc_key[f'{doc_id}'][str(temp)]['pos'].append(i)

        doc_id += 1
        forward_index.update(doc_key)

    json_file.close()

lex_file.close()

with open('forwardIndex.json', 'w') as outfile:
    json.dump(forward_index, outfile)
