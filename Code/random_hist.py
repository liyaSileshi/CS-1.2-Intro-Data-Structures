import random
from histogram import hist_dictionary

def rand(histogram):
    print(histogram)
    # print(histogram.keys())
    #puts the dictionary keys into a list
    #keys = list(histogram.keys())

    
    # keys = list(histogram)
    # print(keys)
    # print(random.choice(keys))
    hist = histogram
    values = list(hist.values())

    print(values)
    # print(hist)
    rand = random.sample(hist.items(), 1)
    print(rand)

    while any(item>0 for item in list(hist.values())):
        for key, value in hist.items():
            # while value > 0:
            if [(key,value)] == rand:
                print(rand)
            #print(key)
            #print(value)
                if value >= 1 and value is not 0:

                    # del histogram[key]
                # else:
                    print(key)
                    hist[key] -= 1
                    values = list(hist.values())
                    print(values)
                    # value -= 1
    print(histogram)

    # for i in list(histogram):
    #     print(i)
    #     print[histogram[i]]


if __name__ == '__main__':

    rand(hist_dictionary())
