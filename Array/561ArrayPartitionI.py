class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        i = 0
        nums.sort()
        for i in range(len(nums)//2):
            sum = sum + nums[i*2]
        return sum
