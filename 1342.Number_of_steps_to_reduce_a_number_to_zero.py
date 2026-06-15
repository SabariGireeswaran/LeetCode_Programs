def numberofsteps(num):
    count = 0
    while num != 0:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num - 1
        count += 1
    
    return count

print(numberofsteps(9))