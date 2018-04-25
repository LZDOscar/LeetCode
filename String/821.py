class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        # index = []
        last, cur = -1, -1
        index = []
        res = []
        for i in range(len(S)):
            if S[i] == C:
                 index.append(i)
        print(index)
        for i in index:
            cur = i
            if last == -1:
                for j in range(i,-1,-1):
                    res.append(j)
            else:
                mid = (cur-last)//2
                if (cur-last) % 2 == 0:
                    for j in range(1,mid):
                        res.append(j)
                    res.append(mid)
                    for j in range(mid-1,-1,-1):
                        res.append(j)
                else:
                    for j in range(1,mid+1):
                        res.append(j)
                    for j in range(mid,-1,-1):
                        res.append(j)
            last = cur
        if index[-1] < len(S)-1:
                 for j in range(1,len(S)-index[-1]):
                    res.append(j)
        return res
