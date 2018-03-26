//这里最多出现次数一定要大于n/2，这是前提假设！
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if(count == 0):
                count = 1
                majority = nums[i]
            elif(nums[i] == majority):
                count += 1
            else:
                count -= 1
        return majority
