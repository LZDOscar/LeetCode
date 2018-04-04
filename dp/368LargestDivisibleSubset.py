class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0 :
            return []
        last = [-1]*len(nums)
        dp = [1]*len(nums)
        nums.sort()
        maxcount, maxi = 0, 0
       
        for i in range(len(nums)):
            curcount, curi = 1, -1
            cur = nums[i]
            for j in range(i):
                if cur % nums[j] == 0:
                    if curcount < dp[j]+1:
                        curcount = dp[j] + 1
                        curi = j
            dp[i] = curcount
            last[i] = curi
            if(maxcount < dp[i]):
                maxcount = dp[i]
                maxi = i
        result = []
        curi = maxi
        while(curi >= 0):
            result.append(nums[curi])
            curi = last[curi]
        return result
