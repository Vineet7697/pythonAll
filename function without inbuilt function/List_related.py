# List-related functions without using inbuilt functions
 
def list_length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count
li=[1,2,3,4,5,6,7,8,9,10]
print(list_length(li))


def list_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total
li=[1,2,3,4,5,6,7,8,9,10]
print(list_sum(li))


def list_max(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val
li=[1,2,3,4,5,6,7,8,9,10]
print(list_max(li))

 
def list_min(lst):
    min_val = lst[0]
    for num in lst:
        if num < min_val:
            min_val = num
    return min_val
li=[1,2,3,4,5,6,7,8,9,10]
print(list_min(li))
 
 
 
def count_occurrences(lst, target):
    count = 0
    for item in lst:
        if item == target:
            count += 1
    return count
li=[1,2,3,2,3,4,5,6,7,4,5,6]
print(count_occurrences(li,5))
 
 
 
 
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst
li=[1,2,3,4,5,6,7,8,9,10]
print(reverse_list(li))


def is_palindrome(lst):
    n = len(lst)
    for i in range(n // 2):
        if lst[i] != lst[n - i - 1]:
            return False
    return True
li=[1,2,3,2,1]
print(is_palindrome(li))


def remove_duplicates(lst):
    unique = []
    for i in lst:
        found = False
        for j in unique:
            if j == i:
                found = True
                break
        if not found:
            unique.append(i)
    return unique
li=[1,32,45,6,9,6,2,3,2,1]
print(remove_duplicates(li))


 
def sort_list(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

li=[1,32,45,6,9,6,2,3,2,1]
print(sort_list(li))
 


def merge_lists(lst1, lst2):
    result = []
    for item in lst1:
        result.append(item)
    for item in lst2:
        result.append(item)
    return result
li1=[1,32,45,6,9,6,2,3,2,1]
li2=[2,4,5,6,87,4,23,7,8]
print(merge_lists(li1,li2))

 
def second_max(lst):
    max1 = lst[0]
    for num in lst:
        if num > max1:
            max1 = num
    max2 = None
    for num in lst:
        if num != max1:
            if max2 is None or num > max2:
                max2 = num
    return max2
li=[2,4,5,6,87,4,23,7,8]
print(second_max(li))



def common_elements(lst1, lst2):
    common = []
    for i in lst1:
        for j in lst2:
            if i == j:
                already_added = False
                for k in common:
                    if k == i:
                        already_added = True
                if not already_added:
                    common.append(i)
    return common
li1=[1,34,4,6,9,6,8,23,2,1]
li2=[2,4,5,6,87,4,23,7,8]
print(common_elements(li1,li2))

 
 
 
def rotate_left(lst, k=3):
    n=len(lst)
    rotated = []
    for i in range(k, n):
        rotated.append(lst[i])
    for i in range(k):
        rotated.append(lst[i])
    return rotated
li=[1,32,45,6,9,6,2,3,2,1]
print(rotate_left(li))


 
def split_even_odd(lst):
    even = []
    odd = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd
li=[1,2,3,4,5,6,7,8,9,10]
print(split_even_odd(li))
 
 
 
 
 
def are_equal(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True
li1=[2,4,5,6,87,4,23,7,8]
li2=[2,4,5,6,87,4,23,7,8]
print(are_equal(li1,li2))

 
 
'''
def list_to_string(lst):
    result = ''
    for ch in lst:
        result += str(ch)
    return result
li=[1,2,3,4,5]
print(list_to_string(li))
'''





def string_to_list(s):
    result = []
    for ch in s:
        result.append(ch)
    return result
str="python"
print(string_to_list(str))
 
 
 
 
def remove_duplicate_characters(s):
    result = ''
    for ch in s:
        found = False
        for r in result:
            if ch == r:
                found = True
                break
        if not found:
            result += ch
    return result
str="progrmmong"
print(remove_duplicate_characters(str))


 
 
def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count
str="python"
print(string_length(str))
 
 
 
def alternate_case(s):
    result = ''
    upper = True
    for ch in s:
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            if upper:
                if 'a' <= ch <= 'z':
                    result += chr(ord(ch) - 32)
                else:
                    result += ch
                upper = False
            else:
                if 'A' <= ch <= 'Z':
                    result += chr(ord(ch) + 32)
                else:
                    result += ch
                upper = True
        else:
            result += ch
    return result
str="programming"
print(alternate_case(str))

 
def reverse_each_word(s):
    result = ''
    word = ''
    for ch in s + ' ':
        if ch != ' ':
            word += ch
        else:
            for i in range(len(word)-1, -1, -1):
                result += word[i]
            result += ' '
            word = ''
    return result.strip()

str="programming"
print(reverse_each_word(str))
