import random
from histogram import hist_dictionary

def rand(histogram):
    print(histogram)
    # print(histogram.keys())
    #puts the dictionary keys into a list
    keys = list(histogram.keys())
    print(keys)
    print(random.choice(keys))
if __name__ == '__main__':

    rand(hist_dictionary())
