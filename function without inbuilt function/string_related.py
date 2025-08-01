# String-related functions without using inbuilt functions

def string_length(s):
    count=0
    for _ in s:
        count+=1
        
    return count
str="python"
print(string_length(str))



def count_char(s, target):
    count = 0
    for ch in s:
        if ch == target:
            count += 1
    return count
str="pythonprogramming"

result=count_char(str,"r")
print(result)


# reverse string using inbuilt function
def reverse_string(s):
    reversed_s = ''
    string_length=len(s)
    for i in range(string_length - 1, -1, -1):
        reversed_s += s[i]
    return reversed_s
str="python"
print(reverse_string(str))



# reverse string without using inbuilt function
def reverse_string(s):
    reversed_s = ''
    for i in range(string_length(s) - 1, -1, -1):
        reversed_s += s[i]
    return reversed_s
def string_length(s):
    count=0
    for _ in s:
        count+=1
    return count
str="python"
print(reverse_string(str))



# palindrome string using inbuilt function
def is_palindrome(s):
     n =len(s)

     for i in range(n // 2):
         if s[i] != s[n - i - 1]:
             return False
     return True
 
str="NAMAN"
print(is_palindrome(str))


# palindrome without using inbuilt function
def is_palindrome(s):
    n = string_length(s)

    for i in range(n // 2):
         if s[i] != s[n - i - 1]:
             return False
    return True
def string_length(s):
    count=0
    for _ in s:
        count+=1
    return count
str="NAMAN"
print(is_palindrome(str))


  
def to_lower_case(s):
    result = ''
    for ch in s:
        if 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result
str="PROGRAM"
print(to_lower_case(str))


def to_upper_case(s):
     result = ''
     for ch in s:
         if 'a' <= ch <= 'z':
             result += chr(ord(ch) - 32)
         else:
             result += ch
     return result
str="program"
print(to_upper_case(str))
 
 
 
 
def remove_spaces(s):
     result = ''
     for ch in s:
         if ch != ' ':
             result += ch
     return result
 
str="python programming"
print(remove_spaces(str))



def count_words(s):
    count = 0
    in_word = False
    for ch in s:
        if ch != ' ' and not in_word:
            count += 1
            in_word = True
        elif ch == ' ':
            in_word = False
    return count
str="python programming is the beginner language "
print(count_words(str))


def replace_char(s, old, new):
    result = ''
    for ch in s:
         if ch == old:
             result += new
         else:
             result += ch
    return result

str="Python"
print(replace_char(str,"t","v"))


# Substring using inbuilt function
def find_substring(s, sub):
    n = len(s)
    m =len(sub)
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if s[i + j] != sub[j]:
                match = False
                break
        if match:
            return i
    return -1
str="python"
print("indexno:",find_substring(str,"y"))


# Substring without using inbuilt function
def find_substring(s, sub):
    n = string_length(s)
    m =string_length(sub)
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if s[i + j] != sub[j]:
                match = False
                break
        if match:
            return i
    return -1
def string_length(s):
    count=0
    for _ in s:
        count+=1
        
    return count
str="python"
print("indexno:",find_substring(str,"n"))





def remove_vowels(s):
    result = ''
    for ch in s:
        if ch not in 'aeiouAEIOU':
            result += ch
    return result
str="python"
print(remove_vowels(str))



def get_unique_characters(s):
    result = ''
    for ch in s:
        exists = False
        for r in result:
            if ch == r:
                exists = True
                break
        if not exists:
            result += ch
    return result
str="programming"
print(get_unique_characters(str))



def char_frequency(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq
str="programming"
print(char_frequency(str))




def capitalize_first_letter(s):
    result = ''
    capitalize = True
    for ch in s:
        if ch == ' ':
            result += ch
            capitalize = True
        elif capitalize and 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
            capitalize = False
        else:
            result += ch
            capitalize = False
    return result
str="program"
print(capitalize_first_letter(str))



