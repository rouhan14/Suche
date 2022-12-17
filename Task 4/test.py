dic1 = {'wordID': {'docID': {'hits': 123}, 'pos': [1,2,3,4,5,6]}}
dic2 = {'doc': {'hits': 12, 'pos': [7,6,5,4,3]}}

dic1['wordID'].update(dic2)

print(dic1)