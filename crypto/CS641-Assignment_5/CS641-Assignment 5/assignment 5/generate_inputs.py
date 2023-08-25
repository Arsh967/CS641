#import random

#rand_num = random.randint(0, 127)
#print(rand_num)

input = [0,0,0,0,0,0,0,0]
#print(input)

with open("input.txt", "w") as f:
    for i in range(8):
        for j in range(0,128):
            input[i]= j
            for elem in input:
                f.write(str(elem) + ' ')
            f.write('\n')
        input[i]=0

