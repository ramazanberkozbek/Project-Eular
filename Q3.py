import math

def isPrime(number):
    is_prime = True
    
    #köküne kadar bakıyoruz ki daha hızlı olsun 
    for i in range(2,int(math.sqrt(number))+1):
        if number % i == 0:
            is_prime = False
            continue
    return is_prime

enBuyukBolen = 1
sayi = 600851475143

sayininYarisi = int(sayi/2)

#Burası biraz şansmış 58 sayısının ebb'si 29 çünkü
#yarıyı almak lazm kökü değil ama o zamanda uzun sürdü
for i in range(2,sayininYarisi+1):
    if isPrime(i) and sayi % i == 0:
            enBuyukBolen = i
            i += 1
    else: 
        i += 1
        
print(enBuyukBolen)