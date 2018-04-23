class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = len(s)
        i, j = 0, 0
        while(i<len(s) and j<len(t)):
            if s[i] == [j]:
                i += 1
            j += 1
        if i == len(s):
            return True
        return False
    
