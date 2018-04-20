class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            a = int(str(x)[::-1])
            if a < 2**31:
                return a
            else:
                return 0
        else:
            a = -int(str(x)[::-1][:-1])
            if a >= -2**31:
                return -int(str(x)[::-1][:-1])
            else:
                return 0
