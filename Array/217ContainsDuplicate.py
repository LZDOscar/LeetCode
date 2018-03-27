class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for i in nums:
            if(dic.get(i) == 1):
                return True
            else:
                dic[i] = 1
        return False
