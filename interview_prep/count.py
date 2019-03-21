file = 'words.txt'

with open(file, 'r') as file:
    for i in file:
        print(i[0:11])
