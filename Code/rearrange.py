import sys
from random import choice





def random_rearrange(words):
    print("words", words)
    temp = words.copy()
    print(temp)
    new_word = []
    while len(temp) > 0:
        print("words", words)
        pick = choice(temp)
        new_word.append(pick)
        temp.remove(pick)
        # print(len(words))
    print("w", words)
    #https://bytes.com/topic/python/answers/794376-printing-contents-list-one-line
    # print(' '.join(item for item in new_word))
    return new_word
    
   
        

if __name__ == '__main__':
    #https://stackoverflow.com/questions/4033723/how-do-i-access-command-line-arguments-in-python
    args = sys.argv[1:]
    if len(args) >= 1 :
        rand = random_rearrange(args)
        print(' '.join(rand))
    else:
        print('not enough words')
