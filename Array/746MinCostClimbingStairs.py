//dp[i] = min(dp[i-1]+cost[i-1] ,dp[i-2]+cost[i-2])  假设dp[i]是上到第i层的最小代价，注意一下循环里边的len+1,因为我们要上到第len+1层
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0]*(len(cost)+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2,len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1] ,dp[i-2]+cost[i-2])
        return dp[-1]
