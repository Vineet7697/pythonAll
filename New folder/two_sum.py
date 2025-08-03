def two_sum(nums,target):
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            if nums[i]+nums[j]==target:
                return [i,j]
li=[2,7,6,8]
target=9
print(two_sum(li,target))