import os

FOLDER_PATH = r'D:\\Sem Projects\\DSA Project\\General Shit\\practise\\dir'

def listDir(dir):
    fileNames =  os.listdir(dir)
    with open('filenames.txt', 'w') as file:
        for fileName in fileNames:
            file.write(fileName + '\n')
            print(fileName)

listDir(FOLDER_PATH)