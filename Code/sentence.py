from word_count import hist_dictionary
from sample import sample_by_frequency
import sys
def sentence(histogram):
    """ 
    Input: dictionary histogram

    Output: sentence from the histogram
    """

    sentence_list = []
    count = 5
    while count > 0:
        sample = sample_by_frequency(dictionary_histogram)
        if sample not in sentence_list:
            sentence_list.append(sample)
            count -= 1
    print(' '.join(sentence_list)+'.')
    return ' '.join(sentence_list) + '.'

if __name__ == '__main__': 
    dictionary_histogram = hist_dictionary(sys.argv[1])
    sentence(dictionary_histogram)
    # sample = sample_by_frequency(dictionary_histogram)
    