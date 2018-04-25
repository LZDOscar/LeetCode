class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x, y = str(bin(x)[2:]), str(bin(y)[2:])
        lenx = len(x)
        leny = len(y)
        count = 0
        if lenx > leny:
            y = '0'*(lenx-leny) + y
        else:
            x = '0'*(leny-lenx) + x
        l = len(x) - 1

        while(l>=0):
            if x[l] != y[l]:
                count += 1
            l -= 1
        return count
            
