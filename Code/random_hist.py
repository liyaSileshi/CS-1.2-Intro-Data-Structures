import random
from histogram import hist_dictionary, hist_list, list_of_words
import sys

def sample_by_frequency(histogram):
    """
    Input: Histogram of text file

    Return : a random word based on the weight(occurence)
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
    words_list = list_of_words(sys.argv[1])
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
    words_list = list_of_words(sys.argv[1])
    histogram  = hist_dictionary(words_list)
    test()
    print(sample_by_frequency(histogram))
