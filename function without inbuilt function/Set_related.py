# Set-related functions without using inbuilt functions
def set_length(s):
    count = 0
    for _ in s:
        count += 1
    return count
s={1,2,3,4,5}
print(set_length(s))



def add_to_set(s, value):
    exists = False
    for item in s:
        if item == value:
            exists = True
            break
    if not exists:
        s.add(value)
    return s
s={1,2,8,3,4,5}
print(add_to_set(s,7))
 
 
def remove_from_set(s, value):
    new_set = set()
    for item in s:
        if item != value:
            new_set.add(item)
    return new_set
s={1,2,3,4,5}
print(remove_from_set(s,3))

 
def is_member(s, value):
    for item in s:
        if item == value:
            return True
    return False
s={1,2,3,4,5}
print(is_member(s,5))


 
def union_sets(s1, s2):
    result = set()
    for item in s1:
        result.add(item)
    for item in s2:
        result.add(item)
    return result
 
s1={1,2,3,4,5,7,9,0}
s2={1,2,6,4,5}
print(union_sets(s1,s2))



  
def intersection_sets(s1, s2):
    result = set()
    for item in s1:
        for other in s2:
            if item == other:
                result.add(item)
    return result
s1={1,2,3,4,5,7,9,0}
s2={1,2,3,4,5}
print(intersection_sets(s1,s2))




def difference_sets(s1, s2):
    result = set()
    for item in s1:
        found = False
        for other in s2:
            if item == other:
                found = True
                break
        if not found:
            result.add(item)
    return result
s1={1,2,3,4,5,7,9,6,14,0}
s2={1,2,6,10,11,4,5}
print(difference_sets(s1,s2))
 

 
def is_subset(s1, s2):
    for item in s1:
        found = False
        for other in s2:
            if item == other:
                found = True
                break
        if not found:
            return False
    return True
s1={1,2,3,4,5,7,9,6,14,0}
s2={1,2,6,10,11,4,5}
print(is_subset(s1,s2))
 
 
#convert_list_to_set without using inbuilt function
def convert_list_to_set(lst):
    result = set()
    for item in lst:
        result = add_to_set(result, item)
    return result
def add_to_set(s, value):
    exists = False
    for item in s:
        if item == value:
            exists = True
            break
    if not exists:
        s.add(value)
    return s
li=[1,2,3,4,5]
print(convert_list_to_set(li))

#convert_list_to_set using inbuilt function
def convert_list_to_set(lst):
    result = set(lst)
    for item in lst:
        result ==item
    return result
li=[1,2,3,4,5]
print(convert_list_to_set(li))
 
 
 
def convert_set_to_list(s):
    result = []
    for item in s:
        result.append(item)
    return result
s={1,2,6,10,11,4,5}
print(convert_set_to_list(s))