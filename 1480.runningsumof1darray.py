def runningsum(nums):
    output = []
    output.append(nums[0])
    for i in range(1,len(nums)):
        sum = output[-1] + nums[i]
        output.append(sum)
    return output

print(runningsum([1,2,3,4]))
