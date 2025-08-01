# Dictionary-related functions without using inbuilt functions
# def dict_length(d):
#     count = 0
#     for _ in d:
#         count += 1
#     return count
# dict = {'a': 1, 'b': 2, 'c': 3}
# print(dict_length(dict))


# def get_keys(d):
#     keys = []
#     for key in d:
#         keys.append(key)
#     return keys
# dict = {'a': 1, 'b': 2, 'c': 3}
# print(get_keys(dict))


 
# def get_values(d):
#     values = []
#     for key in d:
#         values.append(d[key])
#     return values
# dict = {'a': 1, 'b': 2, 'c': 3}
# print(get_values(dict))


 
# def get_items(d):
#     items = []
#     for key in d:
#         items.append((key, d[key]))
#     return items
# dict = {'a': 1, 'b': 2, 'c': 3}
# print(get_items(dict))

 
# def key_exists(d, target):
#     for key in d:
#         if key == target:
#             return True
#     return False
# dict = {'a': 1, 'b': 2, 'c': 3}
# print(key_exists(dict,"b"))


 
# def value_exists(d, target):
#     for key in d:
#         if d[key] == target:
#             return True
#     return False
# dict = {'a': 1, 'b': 2, 'c': 3}
# print(value_exists(dict,3))

 
# def count_value_occurrences(d, target):
#     count = 0
#     for key in d:
#         if d[key] == target:
#             count += 1
#     return count
# dict = {'a': 1, 'b': 2, 'c': 3 , 'd': 3 , 'e': 1}
# print(count_value_occurrences(dict,3))


 
# def add_key_value(d, key, value):
#     d[key] = value
#     return d
# dict = {'a': 1, 'b': 2, 'c': 3}
# print(add_key_value(dict,"d",5))


 
# def update_value(d, key, value):
#     if key_exists(d, key):
#         d[key] = value
#     return d
# def key_exists(d,target):
#     for key in d:
#         if key==target:
#             return True
#     return False
# dict = {'a': 1, 'b': 2, 'c': 3}
# print(update_value(dict,"c",2))



 
# def delete_key(d, target):
#     new_dict = {}
#     for key in d:
#         if key != target:
#             new_dict[key] = d[key]
#     return new_dict
# dict = {'a': 1, 'b': 2, 'c': 3}
# print(delete_key(dict,"c"))

 
# def merge_dicts(d1, d2):
#     merged = {}
#     for key in d1:
#         merged[key] = d1[key]
#     for key in d2:
#         merged[key] = d2[key]
#     return merged
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'d': 4, 'e': 6, 'f': 9}
# print(merge_dicts(dict1,dict2))

 
# def dict_from_list(pairs):
#     d = {}
#     for pair in pairs:
#         key, value = pair
#         d[key] = value
#     return d
# dict = [('a', 1), ('b', 2), ('c', 3)]
# print(dict_from_list(dict))


 
# def invert_dict(d):
#     inverted = {}
#     for key in d:
#         value = d[key]
#         inverted[value] = key
#     return inverted
# dict = {'a': 1, 'b': 2, 'c': 3}
# print(invert_dict(dict))
 


# def dict_get(d, key, default=None):
#     for k in d:
#         if k == key:
#             return d[k]
#     return default
# dict = {'a': 1, 'b': 2, 'c': 3}
# print(dict_get(dict,"t"))
 


 
# def dict_has_key(d, key):
#     for k in d:
#         if k == key:
#             return True
#     return False
# dict = {'a': 1, 'b': 2, 'c': 3}
# print(dict_has_key(dict,"c"))
 
 
 
 
# def dict_update(d1, d2):
#     for key in d2:
#         d1[key] = d2[key]
#     return d1
# dict1 = {'a': 1, 'b': 2, 'c': 8}
# dict2 = {'c': 2, 'e': 5, 'd': 5}
# print(dict_update(dict1,dict2))
 
 
 

 
def dict_copy(d):
    new_d = {}
    for key in d:
        new_d[key] = d[key]
    return new_d
dict = {'a': 2, 'b': 5, 'c': 5}
ans=dict_copy(dict)
print(ans)
print(dict is ans)