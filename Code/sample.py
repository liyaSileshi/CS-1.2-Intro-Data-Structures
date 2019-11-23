import sys
from word_count import hist_dictionary
import random
from tokenize_word import tokens

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

def test():
    """
    A test for sample_by_frequency histogram
    """
    list_of_output = [] 

    words_list = tokens(sys.argv[1])
    print(words_list)
    #change the text file to a dictionary histogram

    histogram = hist_dictionary(words_list)

    #takes a random weighed sample from the histogram 1000x
    #appends it to a list (list_of_output)
    for _ in range(1000):
        list_of_output.append(sample_by_frequency(histogram))

    #changes the list_of_output list to a dictionary histogram
    #prints out the result
    final = hist_dictionary(list_of_output)
    for key in final.keys():
        print(f"{key}: {final[key]}")

if __name__ == '__main__':  
    dictionary_histogram = hist_dictionary(sys.argv[1])

    sample = sample_by_frequency(dictionary_histogram)

    # test()
    