import sys
from random import choice



#https://stackoverflow.com/questions/32470543/open-file-in-another-directory-python/32470564
path = '/usr/share/dict/words'

def rand_dict(num):
    """
        Input: The number of words that user wants generated to form a sentence.
        
        Return: random word from the given dictionary file
    """
    with open(path) as file:
        listr = list(file)
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
    

