import sys
from tokenize import tokens
def hist_dictionary(file_name):
    """
    Input: file name of the source text

    Output: dictionary histogram 
    """
    list_of_words = tokens(file_name)
    dictionary = {}
    for word in list_of_words:
        if word in dictionary :
            dictionary[word] += 1
        else :
            dictionary[word] = 1
    return dictionary
 
if __name__ == '__main__':  
    dictionary_histogram = hist_dictionary(sys.argv[1])
