import numpy


x = 1 
b = int(input('Enter the base of exp. func.: '))
n = int(input('Enter the power of exp. func.: '))
m = int(input('Enter the mod: '))
a = bin(n)
print(a)

power = (b**n) % m
for i in reversed(len(a)):
    print(a)
    if a[i] == 1:
        x = (x*power) % m
    power = (power**power) % m
print (x)


