class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left,right+1):
            s = str(i)
            flag = 0
            for j in s:
                if j == '0' or i % int(j) != 0:
                    flag = 1
                    break
            if not flag:
                res.append(i)
        return res
