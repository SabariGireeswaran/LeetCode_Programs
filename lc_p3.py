from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        length=len(height)
        n=max(height)
        for i in height:
            if i==n:
                line1=i
                break
        h=min(line1,height[length-1])
        index1=height.index(line1)
        index2=length-1
        width=index2 - index1
        area=h*width
        return area
    
object1=Solution()
print(object1.maxArea([1,2,1]))