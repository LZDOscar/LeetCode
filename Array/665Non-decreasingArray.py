class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        if(len(nums) == 0 or len(nums) == 1):
            return True

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if i-2<0 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                    count += 1
                else:
                    nums[i] = nums[i-1]
                    count += 1
            if(count >=2):
                return False
        print(count)
        return True
