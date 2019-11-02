import random
from histogram import hist_dictionary, hist_list, list_of_words

list_of_output = []

def sample_by_frequency(histogram):
    # hist_values = list(histogram.values())
    tokens = sum(histogram.values())
    rand = random.randrange(tokens)
    for key, value in histogram.items():
        if rand < value:
            list_of_output.append(key)
            return key
        rand -= value
  
def test():
    for _ in range(1000):
        words_list = list_of_words()
        histogram = hist_dictionary(words_list)
        sample_by_frequency(histogram)

    return hist_dictionary(list_of_output)
   
if __name__ == '__main__':  
    words_list = list_of_words()
    histogram  = hist_dictionary(words_list)
    print(test())
    print(sample_by_frequency(histogram))
