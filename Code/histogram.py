def histogram():
    with open('alice.txt') as file :
        words = file.read()
        split_words = words.split()
        print(words)
        print(split_words)
        



histogram()