# import nltk
# import json

# from nltk.corpus import stopwords
# stop_words = stopwords.words('english')

# # nltk.data.path.append()

# import panda as pd

# import json
# file = open('D:\\Sem Projects\\DSA Project\\General Shit\\practise\\dir\\911truthorg.json', 'r')


# my_data = json.load(file)
# print(my_data)
# print(type(my_data))


# file.close()

# This removes the stop words from the sentence
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize

# example_text = "This is an exapmmle showing off stop word filtration."

# stop_words = set(stopwords.words("english"))

# words = word_tokenize(example_text)

# filtered_sentence = []

# for w in words:
#     if w not in stop_words:
#         filtered_sentence.append(w)

# print(filtered_sentence)task2.py

# Stemming
# from nltk.stem import PorterStemmer
# from nltk.tokenize import word_tokenize

# ps = PorterStemmer()

# # exapmle_words = ["python", "pyhtoner", "pythoning", "pythoned", "pythonly"]

# # for w in exapmle_words:
# #     print(ps.stem(w))


# new_text = "It is very important to be pythonly while pythoning with python. All pythoners have pythoned poorly."

# words = word_tokenize(new_text)


# for w in words:
#     print(ps.stem(w))


# Regex Removing all special characters
# import re
# re.sub(r'[^\w\s]', "", i)


# Lemmatizing
# from nltk.stem import WordNetLemmatizer

# lemmatizer = WordNetLemmatizer()

# print(lemmatizer.lemmatize('cats'))
# print(lemmatizer.lemmatize("better", pos="a"))
# print(lemmatizer.lemmatize("best", pos="a"))
# print(lemmatizer.lemmatize("run", pos="v"))
# print(lemmatizer.lemmatize('cacti'))
# print(lemmatizer.lemmatize('geese'))
# print(lemmatizer.lemmatize('rocks'))
# print(lemmatizer.lemmatize('python'))


# now writing the original code
# Making a Lexicon

# import os
# import json
# import re
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize, sent_tokenize
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer

# FOLDER_PATH = r'D:\\Sem Projects\\DSA Project\\General Shit\\practise\\dir'

# filenames = os.listdir(FOLDER_PATH)

# ps = PorterStemmer()

# stop_words = set(stopwords.words("english"))

# json_file = open(f'D:\\Sem Projects\\DSA Project\\General Shit\\practise\\dir\\{filenames[0]}', 'r')

# data = json.load(json_file)


# def make_dict_object(id, key):
#     new_dict = {'id': id, 'key': key, 'count': 1}
#     return new_dict


# lexicon = {}
# hits = {}

# lex_id_generator = 0

# id_generator = 0
# for dic in data:
#     sent_title = dic['title'].lower()
#     sent_content = dic['content'].lower()
#     tokenize_title = word_tokenize(sent_title)
#     tokenize_content = word_tokenize(sent_content)
#     tokenize_title = [i for i in tokenize_title if re.sub(r'[^\w\s]', "", i)]
#     tokenize_content = [i for i in tokenize_title if re.sub(r'[^\w\s]', "", i)]

#     for i in range(len(tokenize_title)):
#         tokenize_title[i] = tokenize_title[i].lower()
#         if tokenize_title[i] not in stop_words:
#             ps.stem(tokenize_title[i])
#             lexicon[tokenize_title[i]] = lex_id_generator
#             lex_id_generator += 1
#             # if tokenize_title[i] in lexicon.keys():
#             #     lexicon[tokenize_title[i]]['count'] += 1
#             # else:
#             #     word_obj = make_dict_object(id_generator, 'title')
#             #     id_generator += 1
#             #     lexicon[tokenize_title[i]] = word_obj

#     for i in range(len(tokenize_content)):
#         tokenize_content[i] = tokenize_content[i].lower()
#         if tokenize_content[i] not in stop_words:
#             ps.stem(tokenize_content[i])
#             lexicon[tokenize_content[i]] = lex_id_generator
#             lex_id_generator += 1
#             # if tokenize_content[i] in lexicon.keys():
#             #     lexicon[tokenize_content[i]]['count'] += 1
#             # else:
#             #     word_obj = make_dict_object(id_generator, 'content')
#             #     id_generator += 1
#             #     lexicon[tokenize_content[i]] = word_obj



#     # for word in tokenize_words:
#     #     word = word.lower()
#     #     if word not in stop_words:
#     #         ps.stem(word)
#     #         word_obj = make_dict_object(id_generator, word, 'title')
#     #         id_generator += 1
#     #         lexicon.append(word_obj)

# json_file.close()

# with open("lexicon.json", "w") as outfile:
#     json.dump(lexicon, outfile)



# Agar to key alreadey persent ha to count ki value bharao warna already hua procedure repeat karwao
# Pehla set of data ko dictionary bnao....usko json bnao....usko phir dict bnao....usko phir dict bnao....wtf lkn isse to kuch badly ga hi nahi


# Total articles being crawled through right now: 15365
# Lexicon Creator
import os
import json
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
FOLDER_PATH = r'D:\\Sem Projects\\DSA Project\\General Shit\\practise\\dir'

filenames = os.listdir(FOLDER_PATH)

ps = PorterStemmer()

stop_words = set(stopwords.words("english"))

lexicon = {}

lex_id_generator = 0

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

        for i in range(len(tokenize_title)):
            # tokenize_title[i] = tokenize_title[i].lower()
            if tokenize_title[i] not in stop_words:
                ps.stem(tokenize_title[i])
                if tokenize_title[i] not in lexicon.keys():
                    lexicon[tokenize_title[i]] = lex_id_generator
                    lex_id_generator += 1

        for i in range(len(tokenize_content)):
            # tokenize_content[i] = tokenize_content[i].lower()
            if tokenize_content[i] not in stop_words:
                ps.stem(tokenize_content[i])
                if tokenize_content[i] not in lexicon.keys():
                    lexicon[tokenize_content[i]] = lex_id_generator
                    lex_id_generator += 1

    json_file.close()

with open('lexicon.json', 'w') as outfile:
    json.dump(lexicon, outfile)