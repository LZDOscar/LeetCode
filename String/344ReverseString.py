class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        right = len(s)-1
        r= list(s)
        while(left < right):
            r[left], r[right] = r[right], r[left]
            left += 1
            right -= 1
        return "".join(r)


//use [::-1]
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
