class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        nums.sort()
        Min = float('inf')
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                Sum = nums[i]+nums[left]+nums[right]
                gap = Sum - target
                tmp = Min
                if abs(gap) < abs(Min):
                    Min = gap
                if gap == 0:
                    return target
                elif gap < 0: 
                    left += 1
                else:
                    right -= 1

        return target+Min
