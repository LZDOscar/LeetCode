class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            key = target - nums[i]
            if(key in dic):
                return [dic.get(key), i]
            else:
                dic[nums[i]] = i
