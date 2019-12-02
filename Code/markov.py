import sys
from tokenize_word import tokens
import dictogram
import random

def markov(list_of_words):
    """
    Input: A list of tokens

    Return: A sentence made by the list
    provided using first order
    Markov chain.
    """
    dict_word = {}
    word_list = []
    words = list_of_words
    #for each key, create a list holiding
    # values that comes after it on the original list
    for i in range(len(words)-1):
        if words[i] not in dict_word.keys():
            word_list.append(words[i+1])
            dict_word[words[i]] = word_list
        
        else:
            dict_word[words[i]].append(words[i+1])
        word_list = []
    # print(dict_word)

    #make a nested dictionary using dictogram class
    nested_dict = {}
    for key, value in dict_word.items():
        dict_hist = dictogram.Dictogram(dict_word.get(key))
        nested_dict[key] = dict_hist
    # print(nested_dict)

    #generate sentence
    sentence_list = []
    first_word = random.choice(list(nested_dict.keys()))
    # print("first word: "+first_word)
    sentence_list.append(first_word)
    # print("first word inside: " + str(nested_dict[first_word]))
    dict_inside = nested_dict[first_word]
    # print('weighed sample: ' + dict_inside.sample())
    
    count = 10
    while count > 0:
        dict_inside = nested_dict[first_word]
        next_word = dict_inside.sample()
        sentence_list.append(next_word)
        first_word = next_word
        count -= 1

    # print('Sentence list: ' + str(sentence_list))
    # print('Markov Sentence: ' + ' '.join(sentence_list)+'.')
    # print((' '.join(sentence_list)+'.').capitalize())
    return (' '.join(sentence_list)+'.').capitalize()

if __name__ == '__main__':
    words = tokens('words.txt')
    markov(words)