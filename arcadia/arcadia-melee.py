import numpy as np

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



for k in range(1,9):
    turn = []
    perc = {}
    for i in range(10000):
        i = roll(k)
        if i in perc:
            perc[i] = perc[i] + 1
        else:
            perc[i] = 1
        turn.append(i)
    try:
        
        table = ['Getting 0 hits: ' + str((perc[0]/100) + "%")]
    except:
        table = ['Getting 0 hits: 0.000%']
    for y in range(1,k + 1):
        add = 0
        for i in range(y,k + 1):
            add = perc[i] + add
        table.append('Getting ' + str(y) + " hit(s): " + str(add/100) + "%")
    print(k,'Dice Rolls',table,"\n")





