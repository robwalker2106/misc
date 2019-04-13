import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2106)

number_of_rolls = int(input('How many dice are you rolling?: '))
at_least = int(input('How many blocks are you hoping to get?: '))


def roll(r):

    resluts = []
    

    for x in range(r):
        x = np.random.randint(1,7)
        if x >= 5:
            resluts.append(1)
        else:
            resluts.append(0)    
    return sum(resluts)



turn = []
add = 0
perc = {}

for i in range(10000):
    i = roll(number_of_rolls)
    if i in perc:
        perc[i] = perc[i] + 1
    else:

        perc[i] = 1
    turn.append(i)

print(perc)

for i in range(at_least,number_of_rolls + 1):
    add = perc[i] + add

print('Your change of getting ' + str(at_least) + ' blocks is ' + str(add/10000))


