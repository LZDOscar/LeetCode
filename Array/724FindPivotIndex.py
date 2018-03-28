class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mid = 0
        leftsum = 0
        rightsum = sum(nums)
        for i, val in enumerate(nums):
            rightsum -= val
            if(leftsum == rightsum):
                return i
            leftsum += val
        return -1
