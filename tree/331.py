class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        import re
        last = '#'
        while(preorder):
            preorder =re.sub(r'\d+,#,#','#',preorder)
       
            if preorder == '#':
                return True
            if last == preorder:
                return False
            last = preorder
        return False
        
