import os

# getting the current directory
currentDirectory = os.path.dirname(os.path.realpath(__file__))
# joining the current directory with file name
path = os.path.join(currentDirectory, 'text.txt')
folderPath = os.path.join(currentDirectory, 'test')

if os.path.exists(path):
    print('This file exists')
    if os.path.isfile(folderPath):
        print('This is a file')
    elif os.path.isdir(folderPath):
        print('This is a directory')
else:
    print("This file doesn't eixst")
