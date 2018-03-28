//the version of myself
class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxcount = 0
        count = 0
        for i in range(len(nums)):
            if(i == 0):
                count = 1
            elif(nums[i] - nums[i-1] > 0):
                count += 1
            else:
                maxcount = max(count, maxcount)
                count = 1     
        maxcount = max(count, maxcount)         
        return maxcount


