//the version of myself , but very slow
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        l = [0]*(rowIndex+1)
        for i in range(rowIndex+1):
            if(i == 0):
                l[0] = 1
            elif(i == 1):
                l[1] = 1
            else:
                for j in range(rowIndex,0,-1):
                    l[j] = l[j-1]+l[j]
        return l
                        
                    

//use map,  good idea , too fast

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(rowIndex):
            res = list(map(lambda x,y: x+y, [0]+res, res+[0]))
        return res
                     
