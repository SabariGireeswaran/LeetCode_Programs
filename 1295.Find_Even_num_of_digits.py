def findNumbers(nums):
        digits = []
        count = 0
        for i in nums:
            digit = 0
            while i > 0:
                i = i // 10
                digit += 1
            digits.append(digit)
        print(digits)
        for i in digits:
            if i % 2 == 0:
                count += 1
        
        return count


print(findNumbers([555,901,482,1771]))