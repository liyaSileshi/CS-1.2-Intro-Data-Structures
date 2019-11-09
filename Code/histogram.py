def list_of_words(file_name):
    """Returns the words in a text file in a list format"""
    with open(file_name, 'r') as file :
        words = file.read()
        split_words = words.split()
        return split_words

def hist_dictionary(words):
    """ Retruns the dictionary histogram
         representation of a given list of words"""
    dictionary = {}
    for word in words:
        if word in dictionary :
            dictionary[word] += 1
        else :
            dictionary[word] = 1
    return dictionary
        
def hist_list(words):
    """ Retruns the list of list histogram
         representation of a given list of words"""
    index = 0
    count = 0
    big_list = []
    # starts with all words with a zero value
    # when looping through split words, whenever the word exists,
    # increase value by 1
    for word in words:
        if [word,count] not in big_list :
            big_list.append([word,count])

    for word in words:
        for i in range(len(big_list)) :
            if big_list[i][index] == word :
                big_list[i][1] += 1
    return big_list
       

def hist_tuple(words):
    """ Retruns the list of tuple histogram
         representation of a given list of words"""
    #frequency of each word
    word_freq = []
    for word in words:
        word_freq.append(words.count(word))
        
    #tuple A
    big_tuple = []
    for word in words:
        if (word,words.count(word)) not in big_tuple :
            big_tuple.append((word, words.count(word)))
    return big_tuple

    #tuple B
    #https://programminghistorian.org/en/lessons/counting-frequencies
    tuple_histogram = list(zip(words, word_freq))
    unique_tuple = []
    for pairs in tuple_histogram :
        if pairs not in unique_tuple :
            unique_tuple.append(pairs)

def hist_counts_list(words):
    """ In progress : list of counts histogram..."""
    with open('alice.txt') as file :
        words = file.read()
        split_words = words.split()

        #counts_list
        counts_list = []
        for word in split_words:
            if (split_words.count(word), [word]) not in counts_list:
                for i in counts_list:
                    # if counts_list.index(i)[0] == split_words.count(word):
                    #     counts_list.index(i)[1].append(word)
                    
                    # else:
                    #     counts_list.append((split_words.count(word),[word]))
                    print(counts_list.index(word))


def unique_words_dict(list) :
    """Returns the number of unique words (types) in a list"""
    count = 0
    for _ in list :
        count += 1
    return count

def frequency_dict(word, histogram) :
    return histogram[word]

def write_list(histogram) :
    with open('write_hist.txt', 'w') as file :
        for word in histogram :
            file.write(word[0] + ' ')
            file.write(str(word[1])+ '\n')

def write_dict(histogram) :
    with open('write_dict.txt', 'w') as file :
        for k, v in histogram.items():
            file.write(str(k) + ': '+ str(v) + '\n')

def analysis(histogram): 
    sum = 0
    for word in histogram :
        sum += word[1]
    print(f'sum: {sum}')
    mean = sum/len(histogram)
    print(f'mean: {mean}')

if __name__ == '__main__':
    words = list_of_words('words.txt')
    hist_dict = hist_dictionary(words)
    histogram_list = hist_list(words)
    histogram_tuple = hist_tuple(words)

   
    unique_words_dict(hist_dict)
    # print(frequency_dict('two',hist))
    #analysis(hist)
    # write_dict(hist)
    
