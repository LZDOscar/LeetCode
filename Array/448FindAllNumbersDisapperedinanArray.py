//formal
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        count = [0] * l
        for i in nums:
            count[i-1] += 1
        r = []
        for i in range(len(count)):
            if(count[i] == 0):
                r.append(i+1)
        print (r)
        return r



//use set
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        return list(set(range(1,len(nums)+1)).difference(set(nums)))
