def hist_dictionary():
    with open('alice.txt') as file :
        words = file.read()
        split_words = words.split()
        dictionary = {}
        for word in split_words:
            if word in dictionary :
                dictionary[word] += 1
            else :
                dictionary[word] = 1
        print(dictionary)
        return dictionary
        

def hist_list():
    with open('alice.txt') as file :
        words = file.read()
        split_words = words.split()
        index = 0
        count = 0
        big_list = []
        #all words with a zero value
        #when looping through split words, whenever the word exists,
        #  increase value by 1
        for word in split_words:
            if [word,count] not in big_list :
                big_list.append([word,count])

        for word in split_words:
            for i in range(len(big_list)) :
                if big_list[i][index] == word :
                    # print(word)
                    big_list[i][1] += 1
            # if big_list[index][0] == word:
            #     count += 1
   
        print(big_list)
       
        

def hist_tuple():
    with open('alice.txt') as file :
        words = file.read()
        split_words = words.split()

        #frequency of each word
        word_freq = []
        for word in split_words :
            word_freq.append(split_words.count(word))
        
    
        #tuple
        big_tuple = []
        for word in split_words:
            if (word,split_words.count(word)) not in big_tuple :
                big_tuple.append((word, split_words.count(word)))
        # print(big_tuple)

        #tuple
        #https://programminghistorian.org/en/lessons/counting-frequencies
        tuple_histogram = list(zip(split_words, word_freq))
        # print(tuple_histogram)
        unique_tuple = []
        for pairs in tuple_histogram :
            if pairs not in unique_tuple :
                unique_tuple.append(pairs)

def hist_counts_list():
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
    for key in list :
        count += 1
    print(count)
    return count


def frequency(word, histogram) :
    for i in histogram :
        if i[0] == word:
            return i[1]

def write(histogram) :
    with open('write_hist.txt', 'w') as file :
        for word in histogram :
            file.write(word[0] + ' ')
            file.write(str(word[1])+ '\n')

def analysis(histogram): 
    sum = 0
    for word in histogram :
        sum += word[1]
    print(f'sum: {sum}')
    mean = sum/len(histogram)
    print(f'mean: {mean}')


#What is the least/most frequent word(s)?
#How many different words are used? unique_words(list)
#What is the average (mean/median/mode) frequency of words in the text? 
if __name__ == '__main__':
    hist = hist_dictionary()
    hist_list()
    # print(hist)

    unique_words_dict(hist)
    # print(frequency('fish',hist))
    #analysis(hist)
    #write(hist)

