import math
import functools

#bu ebob ekok sorusus

#2 sayının  ebobunu döndürüyor
def ebob(x,y):
    return math.gcd(x,y)

#ekok döndürüyor iki sayının çarpımı ebob ve ekoklarının çarpımına eşittir'i kullanarak
def ekok(x,y):
    return (x*y) // ebob(x,y)

sayi = 20
liste = range(1,sayi+1)
    
#Bu kod tek tek tüm listeyi hesaplıyor 1,20 sayılarının ekokunu buluyourz 
result = functools.reduce(ekok,liste)

print(result)