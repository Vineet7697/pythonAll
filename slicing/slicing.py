#slicing string
text = "Python Slicing"

print(text[0:6])       
print(text[7:])        
print(text[::-1])  
print(text[1:5])      
print(text[:4])       
print(text[3:])       
print(text[::2])      
print(text[::-1])
print(text[0:5])       
print(text[7:])        
print(text[-7:-1])     
print(text[::-1])      


#slicing list
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:6])     # [2, 3, 4, 5]
print(numbers[:5])      # [0, 1, 2, 3, 4]
print(numbers[5:])      # [5, 6, 7, 8, 9]
print(numbers[::2])     # [0, 2, 4, 6, 8]
print(numbers[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reverse)

#slicing tuple
my_tuple = ('a', 'b', 'c', 'd', 'e')

print(my_tuple[1:4])    # ('b', 'c', 'd')
print(my_tuple[:3])     # ('a', 'b', 'c')
print(my_tuple[-3:])    # ('c', 'd', 'e')

#negative indexing
data = [100, 200, 300, 400, 500]

print(data[-4:-1])      # [200, 300, 400]
print(data[-1])         # 500 (last element)
print(data[-3:])        # [300, 400, 500]

#Slice with Step Value
nums = list(range(10))  # [0, 1, 2, ..., 9]

print(nums[::3])        # [0, 3, 6, 9] (every 3rd element)
print(nums[1:8:2])      # [1, 3, 5, 7] (from index 1 to 7, step 2)
print(nums[::-2])       # [9, 7, 5, 3, 1] (reverse, every 2nd)


#Copying a List Using Slice
original = [1, 2, 3, 4]
copy = original[:]   # makes a shallow copy

print(copy)   