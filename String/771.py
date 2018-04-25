class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        have = {}
        for i in S:
            if i not in have:
                have[i] = 1
            else:
                have[i] += 1
        count = 0
        for j in J:
            if j in have:
                count += have[j]
        return count
        
