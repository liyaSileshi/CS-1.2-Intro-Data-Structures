import sys
from cleanup import clean
def tokens(file_name):
    """
    Input: file name of the source text
    
    Output: list of tokens from a text
    """
    clean_text = clean(file_name)
    split_words = clean_text.split()
    return split_words

if __name__ == '__main__':  
    words_list = tokens(sys.argv[1])
    