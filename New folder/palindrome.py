def palindrome(x):
    temp=x
    rev=0
    while x!=0:
        digit=x%10
        rev=rev*10+digit
        x//=10
    if temp==rev:
        return True
    return False
a = 121
print(palindrome(a))