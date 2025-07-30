
card=input("Enter the card:")
balance=10000
if card=="SBI":
    pin=int(input("Enter the pin:"))
    if pin==1234:
        bank = input("Enter Withdraw, deposite, balancecheck: ").lower()
        if bank=="withdraw":
            n=int(input("Enter the amount:"))
            print("After withdraw your balance is:",balance-n)
        elif bank=="deposite":
            n=int(input("Enter the amount:"))
            print("After withdraw your balance is:",balance+n)
        elif bank=="balancecheck":
            print(balance)
    else:
        print("incorrect pin")       
        
else:
    print("invalid")