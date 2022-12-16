import json
import os
FOLDER_PATH = r'D:\\Sem Projects\\DSA Project\\General Shit\\practise\\dir'

filenames = os.listdir(FOLDER_PATH)

lex_file = open(f'D:\\Sem Projects\\DSA Project\\General Shit\\practise\\Task 3\\lexicon.json')
lex_data = json.load(lex_file)

# print(lex_data)


dic = {'0': [1,2,3,4,5], '1': [], '2': 12}
lis = [1,2,3,4,5]
var = 1

lis.append(89)
print(lis)

print(dic[f'{var}'])
