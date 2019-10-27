def histogram():
    with open('alice.txt') as file :
        words = file.read()
        split_words = words.split()
       
       #unique words
        unique_words = [] 
        for word in split_words:
            if word not in unique_words:
                unique_words.append(word)
        # print(unique_words)

        #frequency of each word
        word_freq = []
        for word in split_words :
            word_freq.append(split_words.count(word))
        # print(word_freq)


        #list
        big_list = []
        for word in split_words:
            if [word,split_words.count(word)] not in big_list :
                big_list.append([word, split_words.count(word)])
        # print(big_list)



        #dictionary
        dictionary = []
        for word in split_words:
            if {word : split_words.count(word)} not in dictionary :
                dictionary.append({word:split_words.count(word)})
        print(dictionary)
        

        #tuple
        big_tuple = []
        for word in split_words:
            if (word,split_words.count(word)) not in big_tuple :
                big_tuple.append((word, split_words.count(word)))
        print(big_tuple)

        #tuple
        #https://programminghistorian.org/en/lessons/counting-frequencies
        tuple_histogram = list(zip(split_words, word_freq))
        # print(tuple_histogram)
        unique_tuple = []
        for pairs in tuple_histogram :
            if pairs not in unique_tuple :
                unique_tuple.append(pairs)


        print(unique_tuple)
        return unique_tuple

        #print(list(split_words,word_freq))

def unique_words(list) :
    count = 0
    for tuple in list :
        #print(tuple[1])
        if tuple[1] == 1 :
            print(tuple[1])
            count += 1
    print(count)
    return count


def frequency(word, histogram) :
    for i in histogram :
        if i[0] == word:
            return i[1]



hist = histogram()
unique_words(hist)
print(frequency('food',hist))

