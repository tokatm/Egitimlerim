import math

def pascalTriangle():
    for i in range(0, 100):
        for j in range(0, i):
            print(math.comb(i, j))

