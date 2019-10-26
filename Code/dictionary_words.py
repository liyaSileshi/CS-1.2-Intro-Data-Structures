import sys
from random import choice

#put it in a function

#https://stackoverflow.com/questions/32470543/open-file-in-another-directory-python/32470564
path = '/usr/share/dict/words'
def rand_dict(num):
    with open(path) as file:
        listr = list(file)
        # listr = [w.replace('\n', '') for w in listr] 
        listr = [word.strip() for word in listr] 
        new = []
        if num <= len(listr):
            while num > 0:
                pick = choice(listr)
                new.append(pick)
                num -= 1
    return new
        
        
if __name__ == '__main__':
    #https://stackoverflow.com/questions/4033723/how-do-i-access-command-line-arguments-in-python
    num = int(sys.argv[1])
    dict_words = rand_dict(num)
    print(' '.join(dict_words)+'.')




# file = open(filename, 'r')
# data= file.read()
# lines = data.splitlines()

# file.read().split('\n')


