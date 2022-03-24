import random
def selcet_median(l, temp_median=random.choice):
    if len(l) % 2 == 1:
        return select(l, len(l) / 2, temp_median)
    else:
        print(2)



def select(l, k, temp_median):

    if len(l) == 1:
        assert k == 0
        return l[0]


    median = temp_median

    lows = [el for el in l if el < median]
    highs = [el for el in l if el > median]
    medians = [el for el in l if el == median]

    if k < len(lows):
        return select(lows, k, random.choice(lows))
    elif k < len(lows) + len(medians):

        return medians[0]
    else:
        return select(highs, k - len(lows) - len(medians), random.choice(highs))

l = [1,11,2,3,7,9,10,12,14]
print(selcet_median(l,random.choice(l)))