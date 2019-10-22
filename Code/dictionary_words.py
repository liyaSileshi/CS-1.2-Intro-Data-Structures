import sys
from random import choice

#https://stackoverflow.com/questions/32470543/open-file-in-another-directory-python/32470564
path = '/usr/share/dict/words'
with open(path) as file:
    
    list = list(file)
   
    list = [w.replace('\n', '') for w in list]
    # print(list)
    # print(' '.join(item for item in list))
    new = []

    
    # num = int(input('Enter how many words you want: '))
    num = int(sys.argv[1])
   
    if num <= len(list):
        while num > 0:
            pick = choice(list)
            new.append(pick)
            list.remove(pick)
            num -= 1
   

    print(' '.join(n for n in new)+'.')
    