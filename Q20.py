def faktoriyel(x):
    sum = 1
    for i in range(1,x+1):
        sum *= i
    return sum
"""
def rakamlarToplami(x):
    x = str(x)
    sum = 0
    for i in x:
        sum += int(i)        
    return sum

print(rakamlarToplami(faktoriyel(100)))"""

print(sum(list(map(int,str(faktoriyel(100))))))