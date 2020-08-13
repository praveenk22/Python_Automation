import numpy as np
import random as r
import sys

if len(sys.argv) == 2:
    n = int(sys.argv[1])
else:
    n = 1

def generate_ticket(n):
    for i in range(n):
        a = np.zeros((3,9))
        l = list(range(1,91))
        row = 0
        column = 0
        num = 0

        for row in range(0,3):
            c = list(range(0,9))
            for i in range(1,6):
                col = c.pop(r.randint(1,len(c)) - 1)
                num = l.pop(r.randint(1,len(l)) -1)
                a[row][col] =  num
        print(a)
        print("\n")

generate_ticket(n)        