class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        maxsum = sum(nums[:k])
        cursum = maxsum
        for i in range(len(nums)-k):
            cursum = cursum - nums[i] + nums[i+k]
            maxsum = max(maxsum, cursum)
        return float(maxsum)/k