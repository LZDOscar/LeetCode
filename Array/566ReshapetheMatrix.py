class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        count = len(nums) * len(nums[0])
        if (count != r * c):
            return nums
        sumlist = []
        for ilist in nums:
            for i in ilist:
                sumlist.append(i)
        newlist = []    
        count = 0
        for i in range(r):
            jlist = []
            for j in range(c):
                jlist.append(sumlist[count])
                count += 1
            newlist.append(jlist)
        return newlist
