import sys
from random import choice, random
import math

def random_rearrange(words):
    """
    Input: list of words from the command line
    
    Return: randomly rearrange the words
    """
    temp = words.copy()
    new_word = []
    while len(temp) > 0:
        pick = choice(temp)
        new_word.append(pick)
        temp.remove(pick)  
    return new_word
    
# https://bost.ocks.org/mike/shuffle/
def fisher_yates(words):
    m = len(words)

    # while there remain elements to shuffle
    while m:
        m -= 1
        # pick a remaining
        remain = math.floor(random() * m)
        # And swap it with the current element
        temp = words[m]
        words[m] = words[remain]
        words[remain] = temp

    return words


if __name__ == '__main__':
    #https://stackoverflow.com/questions/4033723/how-do-i-access-command-line-arguments-in-python
    args = sys.argv[1:]
    if len(args) >= 1 :
        rand = fisher_yates(args)
        #https://bytes.com/topic/python/answers/794376-printing-contents-list-one-line
        # print(' '.join(item for item in new_word))
        print('Fisher yates: '+' '.join(rand))
    else:
        print('not enough words')

    if len(args) >= 1 :
        rand = random_rearrange(args)
        #https://bytes.com/topic/python/answers/794376-printing-contents-list-one-line
        # print(' '.join(item for item in new_word))
        print('Random_rearrange: '+' '.join(rand))
    else:
        print('not enough words')