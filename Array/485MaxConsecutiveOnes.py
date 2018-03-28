class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCount = 0
        curCount = 0
        for i in (nums):
            if i == 1:
                curCount += 1
                if (curCount > maxCount) :
                    maxCount=curCount
            else:
                curCount = 0
             

        return maxCount
