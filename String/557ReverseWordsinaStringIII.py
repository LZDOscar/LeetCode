class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = s.split()
        ss = ''
        for rr in r:
            ss += rr[::-1]
            ss += ' '
        return ss[:-1]
