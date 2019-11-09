from cleanup import clean
import sys
from tokenize import tokens
import dictogram
import random

def markov():

    words = tokens('words.txt')
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
    #make a nested dictionary using the dictogram
    for key, value in dict_word.items():
        dict_hist = dictogram.Dictogram(dict_word.get(key))
        nested_dict[key] = dict_hist
        # print(dict_hist)

    #generate sentence
    first_word = random.choice(list(nested_dict.keys()))
    print("first word: "+first_word)
    # print(first_word.values())
    print("first word inside: ")
    print(nested_dict[first_word])
    
    dict_inside = nested_dict[first_word]
    print('weighed sample: ' + dict_inside.sample())

    next_word = random.choice(list(nested_dict[first_word]))
    print('next_word: '+ next_word)
    # print(dict_word)
    # print(nested_dict)





markov()