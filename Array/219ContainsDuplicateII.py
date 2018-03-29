class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i in range(len(nums)):
            if(nums[i] in dic and i - dic.get(nums[i]) <=k ):
                return True
            else:
                dic[nums[i]] = i
        return False
