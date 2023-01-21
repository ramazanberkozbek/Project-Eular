def Pythagorean(a,b,c):
    if a * a + b * b == c * c:
        print("a:",a,"b:",b,"c",c,"\nProduct:",(a*b*c)) 

for a in range(1,1000):
    for b in range(1,1000-a):
        c = 1000 - a - b
        if a > b:
            Pythagorean(a,b,c)
        else:break
