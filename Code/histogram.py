def histogram():
    with open('alice.txt') as file :
        words = file.read()
        split_words = words.split()
       
        #frequency of each word
        word_freq = []
        for word in split_words :
            word_freq.append(split_words.count(word))
        
        #list
        big_list = []
        for word in split_words:
            if [word,split_words.count(word)] not in big_list :
                big_list.append([word, split_words.count(word)])
        return big_list
        

        #dictionary
        dictionary = []
        for word in split_words:
            if {word : split_words.count(word)} not in dictionary :
                dictionary.append({word:split_words.count(word)})
        # print(dictionary)
        

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


        


def unique_words(list) :
    count = 0
    for tuple in list :
        #print(tuple[1])
        if tuple[1] == 1 :
            # print(tuple[1])
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
    hist = histogram()
    print(hist)
    unique_words(hist)
    print(frequency('hi',hist))
    analysis(hist)
    #write(hist)

