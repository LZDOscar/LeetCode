class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        tb = []
        lr = []
        for i in range(len(grid)):
            tb.append(max(grid[i]))
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid)):
                temp.append(grid[j][i])
            lr.append(max(temp))
        sum = 0

        for i in range(len(grid)):
            for j in range(len(grid)):
               sum += min(tb[i], lr[j]) - grid[i][j]
        return sum
