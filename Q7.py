import math

def isPrime(x): 
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True     

liste = []

i = 1
while len(liste) <= 10_001:
    if isPrime(i):
        liste.append(i)
        i += 1
    i += 1
print(liste[10_000])