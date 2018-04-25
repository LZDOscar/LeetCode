class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        def dfs(i, j, row, col, k, visited, word):
            if i == row or j == col or i < 0 or j < 0 or visited[i][j] or board[i][j] != word[k]:
                return False

            visited[i][j] = 1

            if k == len(word)-1:
                return True

            res = dfs(i+1, j, row, col, k+1, visited, word) or dfs(i-1, j, row, col, k+1, visited, word) or dfs(i, j+1, row, col, k+1, visited, word) or dfs(i, j-1, row, col, k+1, visited, word)

            visited[i][j] = 0
            return res
        
        
        
        row = len(board)
        col = len(board[0])
        visited = []
        for i in range(row):
            visited.append([0]*col)
        for i in range(row):
            for j in range(col):
                if dfs(i, j, row, col, 0, visited, word):
                    return True
        return False
            
            
