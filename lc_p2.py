from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums=nums1+nums2            
        nums.sort()
        n=len(nums)               
        if n%2==0:
            h=int(len(nums)/2)
            median = (nums[h-1]+nums[h])/2
            return median
        else:
            h=int(len(nums)/2)
            median=nums[h]
            return median
        
object1=Solution()
print(object1.findMedianSortedArrays([1,2],[3,4]))
