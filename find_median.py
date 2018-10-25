import heapq
class Solution(object):
    
        
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        self.lo = []
        self.hi = []
        nums = nums1 + nums2
        i = 0
        while i < len(nums):
            self.addNum(nums[i])
            i +=1
            
        if len(nums) % 2 == 0:
            return (float(self.hi[0]) - float(self.lo[0])) /2
        else:
            return float(-self.lo[0])
       
            
    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.lo) > len(self.hi):
            heapq.heappush(self.hi, -heapq.heappushpop(self.lo,-num))
        else:
            heapq.heappush(self.lo, -heapq.heappushpop(self.hi,num))