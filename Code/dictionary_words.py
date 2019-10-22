import sys

with open('words.txt') as file:
    #print(file.read())
    #print(file)
    list = file.readlines()
    # list.append('hi')
    for a in list:
        print (a)
    # num = sys.argv[1]