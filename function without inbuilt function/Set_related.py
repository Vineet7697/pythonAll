# Set-related functions without using inbuilt functions
def set_length(s):
    count = 0
    for _ in s:
        count += 1
    return count



def add_to_set(s, value):
    exists = False
    for item in s:
        if item == value:
            exists = True
            break
    if not exists:
        s.add(value)
    return s
 
 
 
def remove_from_set(s, value):
    new_set = set()
    for item in s:
        if item != value:
            new_set.add(item)
    return new_set


 
def is_member(s, value):
    for item in s:
        if item == value:
            return True
    return False


 
def union_sets(s1, s2):
    result = set()
    for item in s1:
        result.add(item)
    for item in s2:
        result.add(item)
    return result
 
 
  
def intersection_sets(s1, s2):
    result = set()
    for item in s1:
        for other in s2:
            if item == other:
                result.add(item)
    return result



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
 
 
 
def convert_list_to_set(lst):
    result = set()
    for item in lst:
        result = add_to_set(result, item)
    return result
 
 
 
def convert_set_to_list(s):
    result = []
    for item in s:
        result.append(item)
    return result