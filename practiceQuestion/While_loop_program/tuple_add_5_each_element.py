# Write a program to add 5 in each elements in given tuple. 
tu=(10,20,30,40,50)
i=0
ans=()
while i<len(tu):
    ans+=(tu[i]+5,)
    i+=1
print(ans)