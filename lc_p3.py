from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        length=len(height)
        left = 0
        right = length - 1
        max_area = 0

        while left < right:
            h = min(height[left], height[right])
            width = right - left
            area = h* width
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            return max_area

    
object1=Solution()
print(object1.maxArea([1,2,1]))