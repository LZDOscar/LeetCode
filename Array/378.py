class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        l = [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix))]
        l.sort()
        return l[k-1]
