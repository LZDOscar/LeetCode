class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = sorted(nums)
        sta = 0
        end = -1
        i=0
        while(i<len(nums)):
            if(cur[i] != nums[i]):
                sta = i
                break
            i += 1
        i = len(nums)-1
        while(sta<=i):
            if(cur[i] != nums[i]):
                end = i
                break
            i -= 1
        return end-sta+1

//更好的idea 正向遍历寻找需改动的最左边界，反向遍历寻找需改动的最右边界。
class Solution(object):
    def findUnsortedSubarray(self, nums):
        nums = [float('-inf')] + nums + [float('inf')]
        '''find left boundary'''
        left = 0
        while left<len(nums)-1 and nums[left]<=nums[left+1]:
            left += 1
        # return 0 if already sorted ascending
        if left == len(nums)-1:
            return 0
        min_num = min(nums[left+1:])
        while nums[left] > min_num:
            left -= 1
        '''find right boundary'''
        right = len(nums)-1
        while right>0 and nums[right-1]<=nums[right]:
            right -= 1
        # return 0 if sorted descending
        if right == 0:
            return 0
        max_num = max(nums[:right])
        while nums[right] < max_num:
            right += 1
        return right - left - 1
