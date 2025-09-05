#  Write a program to find how many vowels and consonants are present in strings. 

s="python program"
vowel=0
consonant=0
i=0
while i<len(s):
    ch=s[i]
    if ch in 'aeiou':
        vowel+=1
    elif ch in 'bcdfghjklmnpqrstvwxyz':
        consonant+=1
    i+=1
print("vowel=",vowel)
print("consonant=",consonant)
