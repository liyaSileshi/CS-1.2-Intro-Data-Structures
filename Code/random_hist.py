import random
from histogram import hist_dictionary, hist_list, list_of_words
import sys

def sample_by_frequency(histogram):
    # hist_values = list(histogram.values())
    tokens = sum(histogram.values())
    rand = random.randrange(tokens)
    for key, value in histogram.items():
        if rand < value:
            return key
        rand -= value
  
def test():
    list_of_output = [] 
    words_list = list_of_words(sys.argv[1])
    histogram = hist_dictionary(words_list)
    for _ in range(1000):
        list_of_output.append(sample_by_frequency(histogram))

    final = hist_dictionary(list_of_output)
    for key in final.keys():
        print(f"{key}: {final[key]}")
   
if __name__ == '__main__':  
    words_list = list_of_words(sys.argv[1])
    histogram  = hist_dictionary(words_list)
    test()
    print(sample_by_frequency(histogram))
