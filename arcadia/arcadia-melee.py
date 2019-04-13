import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2106)


def roll(r):

    resluts = []
    

    for x in range(r):
        x = np.random.randint(1,7)
        if x <= 3:
            resluts.append(1)
        elif x == 4:
            resluts.append(1)
        else:
            resluts.append(0)    
    return sum(resluts)

turn = []
add = 0
perc = {}

for i in range(10000):
    i = roll(7)
    if i in perc:
        perc[i] = perc[i] + 1
    else:

        perc[i] = 1
    turn.append(i)

for i in range(5,8):
    add = perc[i] + add

    


print(add/10000)
#title = 'Simulation of 10000 6 Melee Rolls'
#x = 'Times Hit'
#y = 'Times Rolled'
#plt.hist(turn)
#plt.title(title)
#plt.xlabel(x)
#plt.ylabel(y)
#plt.show()


