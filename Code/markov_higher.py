import sys
from tokenize_word import tokens
import dictogram
import random

class Markov(dict):
    def __init__(self, words=None, order = 1):
        
        self.types = 0
        self.tokens = 1
        self.order = order
        self.new_function(words, order)

    def new_function(self, words, order):
        for i in range(len(words)- order):
        
            if tuple(words[i: i+order]) not in self.keys():
                self[tuple(words[i: i+order])] = []

            self[tuple(words[i: i+order])].append(tuple(words[ i+1 : i+order+1 ]))
            
        for key in self.keys():
            self[key] = dictogram.Dictogram(self[key])
        # return sekf

    def get_str(self, num):
        start = random.choice(list(self.keys()))
        ret_str = list(start)
        for _ in range(num-self.order):
            next_tuple = self[start].sample()
            ret_str.append(next_tuple[self.order-1])
            start = next_tuple
        return ' '.join(ret_str)



if __name__ == '__main__':
    words = tokens('words.txt')
    # words = ['i', 'went', 'left', 'you', 'went', 'right', 'i','went','left', 'i', 'went', 'right']
    markov_sent = Markov(words, 5)
    for key in markov_sent.keys():
        print(f'{key}: {markov_sent[key]}')
    print(markov_sent.get_str(5))
