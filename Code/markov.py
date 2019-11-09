from cleanup import clean
import sys
from tokenize import tokens
import dictogram

def markov():

    # clean('words.txt')
    words = tokens('words.txt')
    # print(words)
    dict_word = {}
    word_list = []
    for i in range(len(words)-1):
       
        if words[i] not in dict_word.keys():
            word_list.append(words[i+1])
            dict_word[words[i]] = word_list
        
        else:
            dict_word[words[i]].append(words[i+1])
        word_list = []

    nested_dict = {}
    for key, value in dict_word.items():
        dict_hist = dictogram.Dictogram(dict_word.get(key))
        # value = dict_hist
        nested_dict[key] = dict_hist
        print(dict_hist)

    print(dict_word)
    print(nested_dict)
    # print(dict_word.)
    # print(word_list)



markov()