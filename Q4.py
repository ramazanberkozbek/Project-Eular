def isPalindrome(x):
    if numb[0] == numb[-1] and numb[1] == numb[-2] and numb[2] == numb[-3]:
        return True
    else:
        return False

biggestNumber = 1
for i in range(100,1000):
    for j in range(100,1000):
        numb = i * j
        numb = str(numb)
        if isPalindrome(numb):
            if int(numb) >= biggestNumber:
                biggestNumber = int(numb)
            
print(biggestNumber)