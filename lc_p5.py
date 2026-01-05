# LeetCode Problem 5: Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        Rev_num = 0
        n = abs(x)
        
        while n > 0:
            last_digit = n % 10
            Rev_num = (Rev_num * 10) + last_digit
            n = n // 10
        if 2**-31 <= Rev_num <= 2**31 - 1:
            if x < 0:
                Rev_num = - Rev_num
                return Rev_num
            else:
                return Rev_num
        else:
            return 0