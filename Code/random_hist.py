import random
from histogram import hist_dictionary, hist_list

def sample_by_frequency(histogram):
    print(histogram)
    hist_values = list(histogram.values())
    sum = 0
    for value in hist_values:
        sum += value
    #print(sum)
    
    rand = random.randrange(sum)
    print(rand)
    for key, value in histogram.items():
        if rand < value:
            return key
        rand -= value
    #print(fraction)
    print(rand)

    fraction = []
    for value in hist_values:
       frac = (value/sum)*100
       fraction.append(frac)
 

if __name__ == '__main__':  

    print(sample_by_frequency(hist_dictionary()))
   
