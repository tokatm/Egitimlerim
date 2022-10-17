
"""
Created on Sat Oct 24 14:33:35 2020

@author: Mustafa
"""

""" 
    Bir sayinin istenilen modda tersini veren fonksiyon tanimi

"""


x = int(input("the number you want to inverse: "))
m = int(input("mod: "))
sayi = list(range(m))


def modInverse(x,m):
   
    for i in sayi:
        
        k = x*i%m
            
        if k == 1:
                   
            print ("Result:--> ", i)


modInverse(x,m)