# # import os
# # import json
# # from nltk import PorterStemmer, WordNetLemmatizer, pos_tag

# # text = """Welcome you to programming knowledge. Lets start with our first tutorial on NLTK. We shell learn bascis of NLTK here."""
# # demoWords = ['playing', 'happiness', 'going', 'doing', 'yes', 'no', 'I', 'having', 'had', 'haved', 'coding', 'programming', 'code', 'program', 'playing']

# # lematizer = WordNetLemmatizer()
# # ps = PorterStemmer()

# # lemaList = ['a', 's', 'r', 'n', 'v']

# # # print([i for i in lemaList])

# # dic1 = {"name": {"Rouhan": {"type": 'title'}, "Rouhan": {"type": 'content'}}}

# # # temp = {"Rouhan" : {'type': 'content'}}

# # # dic1["name"].update(temp)

# # val = 0
# # if dic1['name']['Rouhan'].keys() == 'type':
# #     print('dsa')

# # print()

# # for word in demoWords:
#     # Left side is the stemmer and the right side is lemmatizer.
#     # print(word, ps.stem(word), lematizer.lemmatize(word, pos=))


# list1 = [1,2,3,4,5,2,3,5,'rouhan']

# if 10 not in list1:
#     print('dsa')


# Number of articles in 'dir' finder
import os
import json

FOLDER_PATH = r'D:\\Sem Projects\\DSA Project\\General Shit\\Suche\\dir'
filenames = os.listdir(FOLDER_PATH)

count = 0

for i in range(len(filenames)):
    json_file = open(
        f'D:\\Sem Projects\\DSA Project\\General Shit\\Suche\\dir\\{filenames[i]}', 'r')

    data = json.load(json_file)

    # number_of_articles += len(data)

    

    for dic in data:
        count += 1

print(count)
