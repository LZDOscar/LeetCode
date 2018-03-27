// the version of myself
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        short = 1
        maxcount = 1
        dic[nums[0]] = [1, 0]
        for i in range(1,len(nums)):
            if(nums[i] in dic):
                l = []
                l = dic.get(nums[i])
                dic[nums[i]] = [l[0]+1, l[1]]
                if(l[0] + 1 > maxcount):
                    dis = i - dic.get(nums[i])[1] + 1
                    short = dis
                    maxcount = dic.get(nums[i])[0]
                elif(l[0] + 1 == maxcount):
                    dis = i - dic.get(nums[i])[1] + 1
                    short = min(short, dis)
            else:
                dic[nums[i]] = [1 ,i]
        return short
            
