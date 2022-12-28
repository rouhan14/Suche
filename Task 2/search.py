import json

# Loading lexicon and inverted index in memory
lexicon_file = open(
    f'D:\\Sem Projects\\DSA Project\\General Shit\\Suche\\Task 2\\lexicon.json')
lexicon_data = json.load(lexicon_file)
lexicon_file.close()

inverted_file = open(
    f'D:\\Sem Projects\\DSA Project\\General Shit\\Suche\\Task 2\\invertedIndex.json')
inverted_data = json.load(inverted_file)
inverted_file.close()

# Doing one word query right now
sentence = input('Search: ')

word_arr = sentence.split()

list_to_be_disp = []
weight = []

dic_found = {}

for word in word_arr:

    if word in lexicon_data and word not in dic_found:
        dic_found = inverted_data[str(lexicon_data[word])]
        for key in dic_found.keys():
            list_to_be_disp.append(key)
            weight.append([int(key), 0])
    else:
        print('No such word found')

print(list_to_be_disp)


if (len(list_to_be_disp) != 0):
    for wordID in range(len(list_to_be_disp)):
        if 'title' in dic_found[list_to_be_disp[wordID]]:
            temp = dic_found[list_to_be_disp[wordID]]['title']
            weight[wordID][1] = 10*temp

        if 'content' in dic_found[list_to_be_disp[wordID]]:
            temp = dic_found[list_to_be_disp[wordID]]['content']
            weight[wordID][1] += 5*temp

# create an empty dictionary to store the merged lists
merged_dict = {}

# iterate through the input list
for lst in weight:
    # if the first element of the list is already in the dictionary
    if lst[0] in merged_dict:
        # add the second element of the list to the value of the first element
        merged_dict[lst[0]] += lst[1]
    # if the first element of the list is not in the dictionary
    else:
        # add the first element as the key and the second element as the value
        merged_dict[lst[0]] = lst[1]

# convert the dictionary to a list of lists
output_weight = [[k, v] for k, v in merged_dict.items()]

# print the output list

output_weight.sort(key=lambda x: x[1], reverse=True)

doc_index_file = open(
    f'D:\\Sem Projects\\DSA Project\\General Shit\\Suche\\Task 2\\docIndex.json')

doc_index = json.load(doc_index_file)
doc_index_file.close()

count = 0
if (len(output_weight) != 0):
    for doc_arr in output_weight:
        if count == 15:
            break
        print(doc_index[str(doc_arr[0])])
