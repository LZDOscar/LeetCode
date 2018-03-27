//the version of myself
class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxnum = nums[0]
        twomaxnum = -1
        maxindex = 0
        for i in range(1,len(nums)):
            if(nums[i] > maxnum):
                twomaxnum = maxnum
                maxnum = nums[i]
                maxindex = i
            elif(nums[i] > twomaxnum):
                twomaxnum = nums[i]
        if(maxnum >= 2*twomaxnum):
            return maxindex
        else:
            return -1


// 2th method
class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 1):
            return 0
        
        a, b = heapq.nlargest(2, nums)
        if(a >= b*2):
            for i in range(len(nums)):
                if(a == nums[i]):
                    return i
        return -1
                
                
