import sys
from word_count import hist_dictionary
import random

def sample_by_frequency(histogram):
    """
    Input: dictionary histogram of a text file

    Return: a weighed random word
    """
    tokens = sum(histogram.values())
    rand = random.randrange(tokens)
    for key, value in histogram.items():
        if rand < value:
            return key
        rand -= value

if __name__ == '__main__':  
    dictionary_histogram = hist_dictionary(sys.argv[1])
    sample = sample_by_frequency(dictionary_histogram)
    