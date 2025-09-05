# (madam=madam) 

s="madam"
reverse=""
for i in s:
    reverse=i+reverse
if s==reverse:
    print("palindrome")
else:
    print("not palindrome")