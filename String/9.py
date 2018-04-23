class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        l = len(s)
        left,right = 0,l-1
        while(left<right):
            if(s[left] != s[right]):
                return False
            left += 1
            right -= 1
        return True
        
