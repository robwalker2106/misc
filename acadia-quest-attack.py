import numpy as np
import matplotlib.pyplot as plt



def roll(r):

    resluts = []
    

    for _ in range(6):
        x = np.random.randint(1,7)
        if x <= 3:
            resluts.append(1)
        elif x == 4:
            resluts.append(1)
        else:
            resluts.append(0)       
    return sum(resluts) > 2

turn = []

for _ in range(10000):
    turn.append(roll(4))


plt.plot(turn)
plt.show()

