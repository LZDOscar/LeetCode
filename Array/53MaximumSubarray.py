//大神算法！
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = nums[0]
        cursum = nums[0]
        for i in nums[1:]:
            cursum = max(cursum+i, i)
            maxsum = max(maxsum, cursum)
        return maxsum
