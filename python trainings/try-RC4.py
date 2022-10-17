
def trytoRC4(key):
    key_lenght = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_lenght])%256
        temp = S[i]
        S[i] = S[j]
        S[j] = temp
    return S
        
def PRGA(S, n):
    i = 0
    j = 0
    key = []

    while n>0:
        n = n-1
        i = (i+1) %256
        temp = S[i]
        S[i] = S[j]
        S[j] = temp

    

trytoRC4()