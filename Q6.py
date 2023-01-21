def sumSquares(x):
    sum = 0
    for i in range(1,x+1):
        sum += i * i
    return sum

def squaresSum(x):
    sum = 0
    for i in range(1,x+1):
        sum += i
    return sum ** 2

print(squaresSum(100) - sumSquares(100))