
# list -> hetrogeneous datatype
# li=list()
# li=[1,2,3,"raj",True]
# li[0]="vineet"
# print(li)

# li=[1,2,3,4,5]
# li.append("12")
# li.append("new")
# li.append("vineet")
# print(li)
# print(type(li))



# li=[1,5,53,65,2,45,2,2]
# print(len(li))
# print(min(li))
# print(max(li))
# print(li.count(2))
# li.sort()
# print(li)


# li=[1,2,3,"raj",True,1,2,3,"raj",True,1,2,3,"raj",True,1,2,3,"raj",True]
# print(len(li))
# for i in range(len(li)):
#     print(li[i])


# li=[1,2,3,4,5,6,7,8,9,10]
# # print(li)
# for i in li:
#     if i%2==0:
#         print(i)

# # for i in range(len(li)):
# #     if(li[i]%2==0):
# #         print(li[i])

# # square of list
# li=[1,2,3,4,5,6,7,8,9,10]
# for i in li:
#     print(i*i)

# addition
# li=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# for i in li:
#     sum=sum+i
# print("sum=",sum)


# greatest element
# li=[5,6,7,9,10,1]
# max=li[0]
# for i in li:
#     if i>max:
#         max=i
# print("greatest number=",max)


# count a number in a list
# li=[1,2,3,45,67,8]
# count=0
# for i in li:
#     count=count+1
# print(count)


# find the given element in a list and return its index
# li=[1,2,2,3]
# k=2
# for i in range (len(li)):
#     if li[i]==k:
        # print(i)
        # break
# print(li.index(2))
    
# count the element present in list
# li=[1,2,1,2,1,1]
# k=1
# count=0
# for i in li:
#     if i==k:
# # for i in range(len(li)):
# #     if li[i]==k:
#         count=count+1
# print(count)

# sort the list
# li=[3,34,6,7,2,9]
# for i in range(len(li)):
#     for j in range(i+1,(len(li))):
#         if li[i]>li[j]:
#             li[j],li[i]=li[i],li[j]
# print(li)


# second largest element in an list

# li=[1,2,3,4,5,6,7]
# for i  in range (2):
#     for j in range(i+1,len(li)):
#         if li[i]<li[j]:
#             li[j],li[i]=li[i],li[j]
# print(li)
# print(li[1])

# kth largest element in an list
# li=[2,4,5,8,1]
# k=int(input("enter the number:"))
# for i in range(k):
#     for j in range(i+1,len(li)):
#         if li[i]<li[j]:
#             li[j],li[i]=li[i],li[j]
            
# print(li[k-1])


# move zero in the end of the list 
# li=[1,0,2,3,0,4]
# j=0
# for i in range(len(li)):
#     if li[i]!=0:
#         li[i],li[j]=li[j],li[i]
#         j+=1
# print(li)



# target sum
# li=[1,2,4,6,3]
# target=8
# for i in range(len(li)):
#     for j in range(i+1,len(li)):
#         if li[i]+li[j]==target:
#             # print(i,j)  #print index
#             # print(li[i],li[j]) #print index value
#             print(target) #print target
            
            
            


# majority element 
# li=[2,2,1,2,2]

# for i in range(len(li)):
#     if(li[i]!=-1):
#         freq=1
#         for j in range(i+1,len(li)):
#             if li[i]==li[j]:
#                 freq+=1
#                 li[j]=-1
#         print("the frquency of li:",li[i],"is",freq)
        
    
    
# highest frequency in string

# s="programming"
# ans={}
# for i in s:
#     if i in ans:
#         ans[i]=ans.get(i)+1
#     else:
#         ans[i]=1
        

# freq=0
# for i in ans:
#     if ans[i]>freq:
#         freq=ans[i]
# for i in ans:
#     if ans[i]==freq:
#         print(f"'{i}':{freq}")
