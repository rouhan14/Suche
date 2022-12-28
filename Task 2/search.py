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
word = input('Enter the word to be searched: ')

list_to_be_disp = []
weight = []

if word in lexicon_data:
    dic_found = inverted_data[str(lexicon_data[word])]
    for key in dic_found.keys():
        list_to_be_disp.append(key)
        weight.append([int(key), 0])

else:
    print('No such word found')

# Weightage dictionary

title_hit = 0
content_hit = 0

print(dic_found)
print(list_to_be_disp)
print(weight)

if (len(list_to_be_disp) != 0):
    for wordID in range(len(list_to_be_disp)):
        print(dic_found[list_to_be_disp[wordID]])
        if 'title' in dic_found[list_to_be_disp[wordID]]:
            temp = dic_found[list_to_be_disp[wordID]]['title']
            weight[wordID][1] = 10*temp

        if 'content' in dic_found[list_to_be_disp[wordID]]:
            temp = dic_found[list_to_be_disp[wordID]]['content']
            weight[wordID][1] += 5*temp

weight.sort(key=lambda x: x[1])

print(weight)


