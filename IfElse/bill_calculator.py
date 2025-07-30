a=int(input("enter the number:"))
if a>=0 and a<50:
    print(a*5)
elif a>=50 and a<100:
    print((a*10)-5)
elif a>=100 and a<=200:
    print((a*15)-500-5)
elif a>200:
    print((a*20)-1500-500-5)
else:
    print("invalid")