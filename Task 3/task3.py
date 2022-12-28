# Creating Inverted Index -----------> Discusing the idea:
# {wordID: docID: {number of hits: integer, positions of hits: [list of positions]}}

# Change the whole logic. It is way too bad

import os
import json
import time


start = time.time()


FOLDER_PATH = r'D:\\Sem Projects\\DSA Project\\General Shit\\Suche\\dir'

filenames = os.listdir(FOLDER_PATH)

inverted_index = {}




# def doc_barrel_generator(doc_id, num_of_hits, pos_list):
#     doc_barrel = {'hits': num_of_hits, 'pos': pos_list}
#     return {doc_id: doc_barrel}


# lex_file = open(f'D:\\Sem Projects\\DSA Project\\General Shit\\Suche\\Task 2\\lexicon.json')
# lex_data = json.load(lex_file)

forward_file = open(f'D:\\Sem Projects\\DSA Project\\General Shit\\Suche\\Task 2\\forwardIndex.json')
forward_data = json.load(forward_file)

# for doc_key in forward_data.keys():

#     # for word_key in forward_data[doc_key].keys():

#     for lex_value in lex_data.values():
#         # Checking if lex_value present in that particular document. This checking is done one by one.
#         # if str(lex_value) in forward_data[doc_key].keys() and str(lex_value) not in inverted_index.keys():
#         #     word_barrel = {str(lex_value): doc_barrel_generator(doc_key, forward_data[doc_key][str(lex_value)]['hits'], forward_data[doc_key][str(lex_value)]['pos'])}
#         if str(lex_value) in forward_data[doc_key].keys() and str(lex_value) not in inverted_index.keys():
#             word_barrel = {str(lex_value): [doc_key]}

#         # If the wordID is present in the respective document being checked and it is also already present in inverted_index then we just update that key.
#         # if str(lex_value) in forward_data[doc_key].keys() and str(lex_value) in inverted_index.keys():
#         #     inverted_index[str(lex_value)].update(doc_barrel_generator(doc_key, forward_data[doc_key][str(lex_value)]['hits'], forward_data[doc_key][str(lex_value)]['pos']))
#         if str(lex_value) in forward_data[doc_key].keys() and str(lex_value) in inverted_index.keys():
#             inverted_index[str(lex_value)].append(doc_key)

for doc_key in forward_data.keys():

    for wordID in forward_data[doc_key].keys():

        word_barrel = {}

        if wordID not in inverted_index.keys():
            word_barrel = {wordID: [doc_key]}
            inverted_index.update(word_barrel)
        else:
            inverted_index[wordID].append(doc_key)

forward_file.close()

with open('invertedIndex.json', 'w') as outfile:
    json.dump(inverted_index, outfile)


end = time.time()

print(end - start)

# writing code for one word query

# one_word = input("Enter the word for one word Query: ")

# one_word_key = lex_data[one_word]

# print(inverted_index[str(one_word_key)])