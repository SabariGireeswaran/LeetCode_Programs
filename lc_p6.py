#9. Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        dup = x
        n = x
        rev = 0
        while n > 0:
            last_digit = n % 10
            rev = (rev * 10) + last_digit
            n = n // 10
        if rev == dup:
            if x < 0 and rev == dup:
                return True
            else:
                return True
        else:
            return False