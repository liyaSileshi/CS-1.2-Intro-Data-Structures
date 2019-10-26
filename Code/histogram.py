def histogram():
    with open('alice.txt') as file :
        words = file.read()
        split_words = words.split()
        print(words)
        print(split_words)
        unique_words = [] 
        for word in split_words:
            if word not in unique_words:
                unique_words.append(word)
       
        print(unique_words)

        word_freq = []
        for word in split_words :
            word_freq.append(split_words.count(word))
        print(word_freq)


        #tuple
        #https://programminghistorian.org/en/lessons/counting-frequencies
        tuple_histogram = list(zip(split_words, word_freq))
        print(tuple_histogram)
        unique_tuple = []
        for pairs in tuple_histogram:
            if pairs not in unique_tuple:
                unique_tuple.append(pairs)


        print(unique_tuple)
        return unique_tuple

        #print(list(split_words,word_freq))

def unique_words(list):
    count = 0
    for tuple in list:
        #print(tuple[1])
        if tuple[1] == 1:
            print(tuple[1])
            count += 1
    print(count)
    return count


def frequency(word, histogram) :
    


hist = histogram()
unique_words(hist)
frequency('hi',)
