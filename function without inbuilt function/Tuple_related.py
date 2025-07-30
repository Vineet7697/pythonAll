# Tuple-related functions without using inbuilt functions
def tuple_length(t):
    count = 0
    for _ in t:
        count += 1
    return count

def count_occurrences(t, target):
    count = 0
    for item in t:
       if item == target:
            count += 1
    return count
 
def find_max(t):
    max_val = t[0]
    for item in t:
        if item > max_val:
            max_val = item
    return max_val
 
def find_min(t):
    min_val = t[0]
    for item in t:
        if item < min_val:
            min_val = item
    return min_val
def tuple_sum(t):
    total = 0
    for item in t:
        total += item
        return total
   
def index_of_element(t, value):
    index = 0
    for item in t:
        if item == value:
            return index
        index += 1
    return -1
def reverse_tuple(t):
    result = ()
    for i in range(tuple_length(t) - 1, -1, -1):
        result += (t[i],)
    return result
 
def convert_list_to_tuple(lst):
    result = ()
    for item in lst:
        result += (item,)
    return result
 
def convert_tuple_to_list(t):
    result = []
    for item in t:
        result.append(item)
    return result
 
def are_tuples_equal(t1, t2):
    if tuple_length(t1) != tuple_length(t2):
        return False
    for i in range(tuple_length(t1)):
        if t1[i] != t2[i]:
            return False
    return True
