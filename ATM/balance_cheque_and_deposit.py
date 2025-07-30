bank = input("Enter Withdraw, deposite, balancecheck: ").lower()

balance=10000

if bank=="withdraw":
    n=int(input("Enter amount: "))
    print("After Withdraw your balance is: ",balance-n)
    
elif bank=="deposite":
    n=int(input("Enter amount: "))
    print("After deposite your balance is: ",balance+n)
    
elif bank=="balancecheck":
    print(balance)
    
    
    
else:
    print("Invalid")