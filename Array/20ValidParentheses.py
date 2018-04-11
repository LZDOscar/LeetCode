class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if(i == '(' or i == '[' or i == '{'):
                stack.append(i)
            if(i == ')'):
                if not stack:
                    return False
                c = stack.pop()
                if c != '(':
                    return False
            if(i == ']'):
                if not stack:
                    return False
                c = stack.pop()
                if c != '[':
                    return False
            if(i == '}'):
                if not stack:
                    return False
                c = stack.pop()
                if c != '{':
                    return False
        if not stack:
            return True
        return False
