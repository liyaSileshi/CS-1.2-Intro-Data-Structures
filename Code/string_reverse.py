import sys
def reverse(word):
    """
    Input: takes in list of words

    """
    old_word = ""
    if len(word) == 1 :
        #Joins the word from a list to a string
        old_word = ''.join(word)
    else:
        old_word = word

    new_word = []
    reverse_word = ""
    while len(old_word) > 0:
        pick = old_word[len(old_word)-1]
        new_word.append(pick)
        old_word = old_word[:-1]
   
    reverse_word = ' '.join(new_word)
    return reverse_word


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) >= 1 :
        print(reverse(args))
    else:
        print('not enough words')
    