class Solution:
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        
        def gcd(a,b):
            if a < b:
                a, b = b, a
            while b!=0:
                a, b = b, a%b
            return a
        import re
        
        nums = re.findall('[+-]?\d+', expression)
        
        
        a, b= 0, 1
        
        for i, j in zip(nums[::2], nums[1::2]):
            i = int(i)
            j = int(j)
            a = a*j + b*i
            b = b*j
            g = gcd(a, b)
            a = a/g
            b = b/g
            
        if(b < 0):
            a = -a
            b = -b
        return '{0}/{1}'.format(int(a), int(b))



// use fraction
class Solution:
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        
        import re
        from fractions import Fraction
        result = sum(map(Fraction, re.findall('[+-]?\d+/\d+', expression)))
        return '{0}/{1}'.format(result.numerator, result.denominator)
