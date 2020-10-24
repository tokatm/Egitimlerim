# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:33:35 2020

@author: Mustafa
"""

""" 
    Bir sayinin istenilen modda tersini veren fonksiyon tanimi

"""


x = int(input("the number you want to inverse: "))
m = int(input("mod: "))
sayi = list(range(26))


def modInverse(x,m):
    for i in sayi:
        if (x*i%m == 1):
           print(i)
    
modInverse(x,m)





