class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l = []
        for i in range(numRows):
            if(i == 0):
                l.append([1])
            elif(i == 1):
                l.append([1,1])
            else:
                cur = [1]
                for j in range(len(l[i-1])-1):
                    cur.append(l[i-1][j]+l[i-1][j+1])
                cur.append(1)
                l.append(cur)
        return l
