nums = [1,1,1,2,2,3]
k = 2
nums.sort()
repetition = []
for i in range(len(nums)):
    if nums[i] in nums:
        repetition.append(nums[i])
repetition.sort()
print(repetition)