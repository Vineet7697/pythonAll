def sqrt(n):
    i=1
    while i<=n//2:
        if i*i==n:
            return i
        i+=1
    return "not valid"
n=25
print(sqrt(n))