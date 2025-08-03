def anagram(r,t):
    if len(r)!=len(t):
        return False
    if sorted(s1)==sorted(s2):
        return True
    return False

s1="listen"
s2="silent"
print(anagram(s1,s2))