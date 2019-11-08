from cleanup import clean
import sys
from tokenize import tokens

def markov():
    # clean('words.txt')
    words = tokens('words.txt')
    # print(words)
    dict = {}
    word_list = []
    for i in range(len(words)-1):
        # if words[i] in dict.keys() and dict[words[i]] not in word_list:
            # word_list.append(dict[words[i]])
            # print(word_list)
            # dict[words[i]].append(words[i+1])
        # if words[i+1] not in word_list:
        #     word_list.append(words[i+1])
        #     dict[words[i]] = word_list
        
        # else:
        # else:
            # dict[words[i]] = words[i+1]
        # print(dict)
        if words[i] not in dict.keys():
            word_list.append(words[i+1])
            dict[words[i]] = word_list
        # else:
        else:
            # word_list.append()
            dict[words[i]].append(words[i+1])

        word_list = []


    print(dict)
    print(word_list)



markov()