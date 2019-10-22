import sys
from random import choice


#https://stackoverflow.com/questions/4033723/how-do-i-access-command-line-arguments-in-python
args = sys.argv[1:]


def random_rearrange(words):
    new_word = []
    while len(words) > 0:
       
        pick = choice(words)
        new_word.append(pick)
        words.remove(pick)
        # print(len(words))
    
    #https://bytes.com/topic/python/answers/794376-printing-contents-list-one-line
    print(' '.join(item for item in new_word))
        

if __name__ == '__main__':
    random_rearrange(args)
