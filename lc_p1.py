#1. Two sum 
nums=[9,12,1,3,2,6,4,9]
target=int(input("Enter a number:"))
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        value=nums[i]+nums[j]
        if value==target:
            out=[i,j]
            break
print(out)