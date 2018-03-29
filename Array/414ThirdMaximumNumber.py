//最普通的做法是维护一个有三个值的列表，分别保存前三大的数，遍历整个nums，并更新这个列表就OK
class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(set(nums)) < 3):
            return max(nums)
        _,_, result = heapq.nlargest(3,set(nums))
        return result
