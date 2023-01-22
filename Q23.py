"""
Info:
    A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
    For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

    A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
    All integers greater than 28123 can be written as the sum of two abundant numbers. 

Q:
    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

"""
Bilgi:
    Mükemmel sayı bölenlerin toplamı kendisine eşit sayı
    Eksik sayı bölenlerin toplamı kendinden küçük sayı
    Artık sayı bölenlerin toplamı kendinden büyük sayı
    12 en küçük artık sayı (1,2,3,4,6 = 16)
    24 en küçük, 2 artık sayının toplamı
    28123 den sonraki her sayı artık sayıların toplamı olarak yazılabilir

Soru:
    2 artık sayının toplamı olmayan tüm sayıların toplamını bul
"""
"""
import math

def bolenToplamı(x):
    #Bolen sayıların toplamını döndüren fonks 
    toplam = 1
    while n < math.ceil(math.sqrt(x)):
        """
        
"""def divisor(x):
    divs = [1]
    for i in range(2, int(x ** 1/2)+1):
        if x % i == 0:
            divs.append(i)
            if i != x//i:
                divs.append(x//i)
    return divs

print(divisor(12))"""
import math

def divisors(x):
    divs = [1]
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            divs.append(i)
            if i != x//i: #this code adds other multiplier
                divs.append(x//i)
    return divs

def is_abundant(x):
    return sum(divisors(x)) > x #if sum of divisor higher then x return True

abundant_nums = [x for x in range(12, 28123) if is_abundant(x)] #i create a list of abundant nums

not_sum_of_two_abundant = [True] * 28123 #I assumed all the numbers up to x were the answers


#I found all the abundant numbers to 28123 at the top, here I add those numbers with brute force and mark them to the 'not_sum_of_two_abundant list'
for i in range(len(abundant_nums)):
    for j in range(i, len(abundant_nums)):
        if abundant_nums[i] + abundant_nums[j] < 28123:
            not_sum_of_two_abundant[abundant_nums[i] + abundant_nums[j]] = False
        else:
            break

print(sum([i for i in range(1, 28123) if not_sum_of_two_abundant[i]])) #Here, I check the numbers from 1 to 28123 in the list and calculate the sum of the True values.