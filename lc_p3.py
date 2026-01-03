from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        length=len(height)
        left = 0
        right = length - 1

        while left < right:
            height = min(height[left], height[right])
            width = right - left
            area = height * width
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            return area

    
object1=Solution()
print(object1.maxArea([1,2,1]))