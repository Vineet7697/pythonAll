# Tuple-related functions without using inbuilt functions
# def tuple_length(t):
#     count = 0
#     for _ in t:
#         count += 1
#     return count
# tu=(1,2,3,4,8)
# print(tuple_length(tu))




# def count_occurrences(t, target):
#     count = 0
#     for item in t:
#        if item == target:
#             count += 1
#     return count
# tu=(1,2,4,2,3,7,9,6,9,3,4,8)
# print(count_occurrences(tu,4))

 
 
 
# def find_max(t):
#     max_val = t[0]
#     for item in t:
#         if item > max_val:
#             max_val = item
#     return max_val
# tu=(1,2,3,4,8)
# print(find_max(tu))
 
 
 
 
# def find_min(t):
#     min_val = t[0]
#     for item in t:
#         if item < min_val:
#             min_val = item
#     return min_val
# tu=(1,2,3,4,5,)
# print(find_min(tu))



# def tuple_sum(t):
#     total = 0
#     for item in t:
#         total += item
#     return total
# tu=(1,2,3,4,5,)
# print(tuple_sum(tu))


    

   
# def index_of_element(t, value):
#     index = 0
#     for item in t:
#         if item == value:
#             return index
#         index += 1
#     return -1
# tu=(1,2,3,4,5,)
# print("index no:",index_of_element(tu,4))




# def reverse_tuple(t):
#     result = ()
#     tuple_length=len(t)
#     for i in range(tuple_length - 1, -1, -1):
#         result += (t[i],)
#     return result
# tu=(1,2,3,4,5,)
# print(reverse_tuple(tu)) 
 
 
 
'''
def convert_list_to_tuple(lst):
    result = ()
    for item in lst:
        result += (item,)
    return result
li=[1,2,3,4,5]
print(convert_list_to_tuple(li))

'''


# def convert_tuple_to_list(t):
#     result = []
#     for item in t:
#         result.append(item)
#     return result
# tu=(1,2,3,4,5,)
# print(convert_tuple_to_list(tu)) 


 
def are_tuples_equal(t1, t2):
    if len(t1) != len(t2):
        return False
    for i in range(len(t1)):
        if t1[i] != t2[i]:
            return False
    return True
tu1=(1,4,56,7,2,34,76,9,3,84,6,8,4,3)
tu2=(1,4,56,7,2,34,76,9,3,84,6,8,4,3)
print(are_tuples_equal(tu1,tu2))