import numpy as np

np.random.seed(2106)

number_of_rolls = int(input('How many dice are you rolling?: '))


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
perc = {}



for i in range(10000):
    i = roll(number_of_rolls)
    if i in perc:
        perc[i] = perc[i] + 1
    else:

        perc[i] = 1
    turn.append(i)

table = ['Getting 0 hits: ' + str((perc[0]/10000))]

for y in range(1,number_of_rolls + 1):
    add = 0
    for i in range(y,number_of_rolls + 1):
        add = perc[i] + add
    table.append('Getting ' + str(y) + " hit(s): " + str(add/10000))

print(table)





