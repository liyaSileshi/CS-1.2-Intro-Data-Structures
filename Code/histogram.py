import json
def list_of_words(file_name):
    with open(file_name, 'r') as file :
        words = file.read()
        split_words = words.split()
        return split_words

def hist_dictionary(words):
    dictionary = {}
    for word in words:
        if word in dictionary :
            dictionary[word] += 1
        else :
            dictionary[word] = 1
    return dictionary
        
def hist_list(words):
    index = 0
    count = 0
    big_list = []
    '''all words with a zero value
    when looping through split words, whenever the word exists,
    increase value by 1'''
    for word in words:
        if [word,count] not in big_list :
            big_list.append([word,count])

    for word in words:
        for i in range(len(big_list)) :
            if big_list[i][index] == word :
                big_list[i][1] += 1
    # print(big_list)
    return big_list
       
def hist_tuple(words):
    #frequency of each word
    word_freq = []
    for word in words:
        word_freq.append(words.count(word))
        
    #tuple
    big_tuple = []
    for word in words:
        if (word,words.count(word)) not in big_tuple :
            big_tuple.append((word, words.count(word)))
        # print(big_tuple)

    #tuple
    #https://programminghistorian.org/en/lessons/counting-frequencies
    tuple_histogram = list(zip(words, word_freq))
    # print(tuple_histogram)
    unique_tuple = []
    for pairs in tuple_histogram :
        if pairs not in unique_tuple :
            unique_tuple.append(pairs)

def hist_counts_list(words):
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

       # print('counts list: ')
        #print(counts_list)
        # print(counts_list[1][0])

def unique_words_dict(list) :
    count = 0
    for _ in list :
        count += 1
    print(count)
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
    #    file.write(json.dumps(histogram))
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
    hist = hist_dictionary(list_of_words())
    # hist_list(list_of_words())
    # print(hist)
    # unique_words_dict(hist)
    # print(frequency_dict('two',hist))
    #analysis(hist)
    write_dict(hist)
