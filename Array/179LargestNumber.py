class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        from functools import cmp_to_key

        nums = sorted(map(str,nums),key= cmp_to_key(lambda x,y: int(y+x)-int(x+y)))
        
        return "".join(nums).lstrip('0') or '0'
        
