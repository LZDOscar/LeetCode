class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1 = len(num1)
        len2 = len(num2)
        result = [0]*(len1+len2-1)
        flag = 0
        
        if(num1[0] == '0' or num2[0]=='0'):
            return '0'
        
        for i in range(len1):
            for j in range(len2):
                result[i+j] += int(num1[i]) * int(num2[j])

        for i in range(len1+len2-2, -1, -1):
            result[i] += flag
            flag = result[i] // 10
            result[i] = result[i] % 10
            
        result = "".join(list(map(str, result)))
      
        if (flag):
            return str(flag)+result
        return result
                
