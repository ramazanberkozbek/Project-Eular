def isPalindrome(x:int=0):
    reversed_num = 0
    num = x
    while x != 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    if reversed_num == num:
        return True
    return False    
    
print(isPalindrome(123))