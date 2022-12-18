# Agar to key alreadey persent ha to count ki value bharao warna already hua procedure repeat karwao
# Pehla set of data ko dictionary bnao....usko json bnao....usko phir dict bnao....usko phir dict bnao....wtf lkn isse to kuch badly ga hi nahi


# Total articles being crawled through right now: 15365
# Lexicon Creator
import os
import time
import json
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
FOLDER_PATH = r'D:\\Sem Projects\\DSA Project\\General Shit\\Suche\\dir'


def wordID_maker(hit, string):
    wordID = {'pos': [], 'hits': hit, 'type': string}
    return wordID


filenames = os.listdir(FOLDER_PATH)

ps = PorterStemmer()

wordnet = WordNetLemmatizer()

stop_words = set(stopwords.words("english"))

lexicon = {}

forward_index = {}

lex_id_generator = 0

doc_id = 0

start = time.time()

for i in range(len(filenames)):
    json_file = open(f'D:\\Sem Projects\\DSA Project\\General Shit\\Suche\\dir\\{filenames[i]}', 'r')

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

        doc_key = {f'{doc_id}': {}}



        for i in range(len(tokenize_title)):
            if tokenize_title[i] not in stop_words:
                wordnet.lemmatize(ps.stem(tokenize_title[i]))
                tokenize_title_less_stop_words.append(tokenize_title[i])
                if tokenize_title[i] not in lexicon.keys():
                    lexicon[tokenize_title[i]] = lex_id_generator
                    lex_id_generator += 1

        for i in range(len(tokenize_title_less_stop_words)):
            if tokenize_title_less_stop_words[i] in lexicon.keys() and str(lexicon[f'{tokenize_title_less_stop_words[i]}']) not in doc_key[f'{doc_id}'].keys():
                doc_key[f'{doc_id}'].update({str(lexicon[f'{tokenize_title_less_stop_words[i]}']): wordID_maker(0, 'title')})

            if str(lexicon[f'{tokenize_title_less_stop_words[i]}']) in doc_key[f'{doc_id}'].keys():
                temp = str(lexicon[f'{tokenize_title_less_stop_words[i]}'])
                val = doc_key[f'{doc_id}'][str(temp)]['hits'] + 1
                doc_key[f'{doc_id}'][str(temp)]['hits'] = val

            temp2 = str(lexicon[f'{tokenize_title_less_stop_words[i]}'])
            if str(lexicon[f'{tokenize_title_less_stop_words[i]}']) in doc_key[f'{doc_id}'].keys() and doc_key[f'{doc_id}'][str(temp2)]['type'] == 'title':
                doc_key[f'{doc_id}'][str(temp)]['pos'].append(i)

        for i in range(len(tokenize_content)):
            if tokenize_content[i] not in stop_words:
                wordnet.lemmatize(ps.stem(tokenize_content[i]))
                tokenize_content_less_stop_words.append(tokenize_content[i])
                if tokenize_content[i] not in lexicon.keys():
                    lexicon[tokenize_content[i]] = lex_id_generator
                    lex_id_generator += 1

        for i in range(len(tokenize_content_less_stop_words)):
            if tokenize_content_less_stop_words[i] in lexicon.keys() and str(lexicon[f'{tokenize_content_less_stop_words[i]}']) in doc_key[f'{doc_id}'].keys() and doc_key[f'{doc_id}'][str(temp)]['type'] == 'title':
                doc_key[f'{doc_id}'][str(temp)]['type'] = 'both'

            if tokenize_content_less_stop_words[i] in lexicon.keys() and str(lexicon[f'{tokenize_content_less_stop_words[i]}']) not in doc_key[f'{doc_id}'].keys():
                doc_key[f'{doc_id}'].update(
                    {str(lexicon[f'{tokenize_content_less_stop_words[i]}']): wordID_maker(0, 'content')})

            if str(lexicon[f'{tokenize_content_less_stop_words[i]}']) in doc_key[f'{doc_id}'].keys():
                temp = str(lexicon[f'{tokenize_content_less_stop_words[i]}'])
                val = doc_key[f'{doc_id}'][str(temp)]['hits'] + 1
                doc_key[f'{doc_id}'][str(temp)]['hits'] = val

            temp2 = str(lexicon[f'{tokenize_content_less_stop_words[i]}'])
            if str(lexicon[f'{tokenize_content_less_stop_words[i]}']) in doc_key[f'{doc_id}'].keys() and doc_key[f'{doc_id}'][str(temp2)]['type'] == 'content' or 'both':
                doc_key[f'{doc_id}'][str(temp)]['pos'].append(i)

        doc_id += 1
        forward_index.update(doc_key)

    json_file.close()


inverted_index = {}


for pavilion in forward_index.keys():

    for wordID in forward_index[pavilion].keys():

        word_barrel = {}

        if wordID not in inverted_index.keys():
            word_barrel = {wordID: [pavilion]}
            inverted_index.update(word_barrel)
        else:
            inverted_index[wordID].append(pavilion)

with open('invertedIndex.json', 'w') as outfile:
    json.dump(inverted_index, outfile)


with open('lexicon.json', 'w') as outfile:
    json.dump(lexicon, outfile)

with open ('forwardIndex.json', 'w') as outfile:
    json.dump(forward_index, outfile)


end = time.time()

print(end - start)




# New Concept:
# Dictionary k ander dictionary:
# {docID: [
#           wordID: { hits: int }
#           wordID: { hits: int }
#           wordID: { hits: int }
#         ]
# }
