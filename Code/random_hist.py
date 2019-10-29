import random
import numpy
from histogram import hist_dictionary, hist_list

def rand(histogram):
    print(histogram)
    # print(histogram.keys())
    #puts the dictionary keys into a list
    #keys = list(histogram.keys())

    
    keys = list(histogram)
    print(keys)
    # print(random.choice(keys))
    # hist = histogram
    #accumulated_values = []


    values = list(histogram.values())
    sum = 0
    for value in values:
        sum += value
    print(sum)

    fraction = []
    # deci = []
    for value in values:
       frac = (value/sum)*100
       fraction.append(frac)

    # for i in fraction:
    #     floats = 

    print(fraction)

    random.choices(keys,p=fraction)
    # weighted_random = ['x'] * 1 + ['Y'] * 9 + ['Z'] * 90
    # print(weighted_random)
    # print(random.choice(weighted_random))
   # print(sum(fraction))
    # remaining_distance = random.random() * sum(fraction)
    # print(remaining_distance)



    # for i in range(len(values)):
    #     accumulated_values.append(values[i]+values[i+1])
    #print(value)
    #print(accumulated_values)
    # print(hist)
    #rand = random.sample(hist.items(), 1)
    #print(rand)

    # while any(item>0 for item in list(hist.values())):
    #     for key, value in hist.items():
    #         # while value > 0:
    #         if [(key,value)] == rand:
    #             #print(rand)
    #         #print(key)
    #         #print(value)
    #             if value >= 1 and value is not 0:

    #                 # del histogram[key]
    #             # else:
    #                 #print(key)
    #                 hist[key] -= 1
    #                 values = list(hist.values())
    #                 print(values)
    #                 # value -= 1
    # print(histogram)

    # for i in list(histogram):
    #     print(i)
    #     print[histogram[i]]

def choice_random(histogram):
    rand= random.choices(histogram, weights = [0.125,0.5,0.125,0.125,0.125], k=10)
    print(rand)
    # rand.choice(rand)


if __name__ == '__main__':  

    rand(hist_dictionary())
    # choice_random(hist_list)
    # print(random.randint(1,8))
