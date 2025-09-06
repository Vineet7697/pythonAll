# Python program to check the validity of password input by users. 

password=input("Enter the number:")
upper=False
lower=False
digit=False
special_char=False
special_character="@#$&*!%"

for i in password:
    if i.isupper():
        upper=True
    elif i.islower():
        lower=True
    elif i.isdigit():
        digit=True
    elif i in special_character:
        special_char=True

if len(password)>8 and upper and lower and digit and special_char:
    print("valid password")
else:
    print("Not valid password")