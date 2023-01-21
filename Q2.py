a = 1
b = 2

sum = 2
while True:
    #C ye yeni sayıyı atıyorum b ye eski sayıyı a geçiş sayısını tutuyor kısaca c = fib(x - 1) + fib(x - 2)
    #Örnek fib(5) = fib (4) + fib(3)
    #      c      = b       + a  
    c = a + b
    #3 = 1 + 2
    #5 = 2 + 3
    a = b
    b = c
    if (c % 2 == 0):
        sum += c
    if sum >= 4_000_000:
        break
print(sum)

#2. Çözüm
"""def fib(a):
    if a==0 or a==1:
        return 1
    else:
        return fib(a-1) + fib(a-2)
x=0
sum=0
while fib(x) < 4000000:
    if fib(x) % 2 == 0:
        sum += fib(x)
        x += 1
    else:
        x+=1
print(sum)"""