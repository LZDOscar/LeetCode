//递归
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        def DFS(i, j):
            if(0<= i < m and 0<=j<n and grid[i][j]):
                grid[i][j] = 0
                return 1 + DFS(i+1, j) + DFS(i, j+1) + DFS(i-1, j) + DFS(i, j-1)
            return 0
        maxArea = 0 
        for i in range(m):
            for j in range(n):
                CurArea = DFS(i, j)
                if(CurArea > maxArea):
                    maxArea = CurArea
        return maxArea
                


//栈循环
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        maxCount = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if(0<=i<m and 0<=j<n and val):
                    grid[i][j] = 0
                    count = 0
                    stack = [(i,j)]
                    while(stack):
                        ni,nj = stack.pop()
                        count += 1
                        for nni, nnj in [(ni+1,nj),(ni-1,nj),(ni,nj+1),(ni,nj-1)]:
                            if(0<=nni<m and 0<=nnj<n and grid[nni][nnj]):
                                stack.append((nni, nnj))
                                grid[nni][nnj] = 0

                    print (count)
                    maxCount = max(count, maxCount)
        return maxCount
