x = int(input("Enter #"))
sumDigits = x ** 1000
sum = 0

for i in str(sumDigits):
    sum += int(i)
print(sum)

