# data={
#     "name":"vineet",
#     "roll no":101,
#     100:200,
# }
# data[1000]=100
# for i,j in data.items():
#     print(i,j)


# frequency of character
# s="helloworldpython"
# ans={}
# for i in s:

#     if i in ans:
#         ans[i]=ans.get(i)+1
#     else:
#         ans[i]=1

#     # ans[i]=ans.get(i,0)+1
# print(ans)



# find the frequency of each element present in list
# li=["raj","suraj","raj","ram"]
# ans={}
# for i in li:
#     ans[i]=ans.get(i,0)+1
# print(ans)


# find the student with highest marks
# data={"jatin":55, "raj":90, "rahul":80}
# max=0
# for i in data:
#     if data[i]>max:
#         max=data[i]
#         ans=i
# print(ans)

# # anagram
# s1="anagram"
# s2="graaanm"
# if len(s1)!=len(s2):
#     print("not an anagram")
# else:
#     ans={}
#     for i in s1:
#         ans[i]=ans.get(i,0)+1
#     for j in s2:
#         if j in ans:
#             ans[j]-=1
#     freq=True
#     for i in ans.values():
#         if i!=0:
#             freq=False
#     if ans:
#         print("anagram")
#     else:
#         print("not an anagram")
            
    # roman 
    
roman={
      "I":1,
      "V":5,
      "X":10,
      "L":50,
      "C":100,
      "D":500,
      "M":1000  
}
s="MCMXIV"
ans=0
for i in range(len(s)-1):
    if roman[s[i]]<roman[s[i+1]]:
        ans-=roman[s[i]]
    else:
        ans+=roman[s[i]]
ans=ans+roman[s[len(s)-1]]
print(ans)