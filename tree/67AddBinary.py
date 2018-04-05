class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num1 = a
        num2 = b
        len1 = len(num1)-1
        len2 = len(num2)-1
        result = ''
        flag = 0
        while(len1>=0 and len2>=0):
            temp = int(num1[len1]) + int(num2[len2]) + flag
            flag = temp // 2
            temp = temp % 2
            result += str(temp)
            len1 -= 1
            len2 -= 1
        while(len1>=0):
            temp = int(num1[len1]) + flag
            flag = temp // 2
            temp = temp % 2
            result += str(temp)
            len1 -= 1
        while(len2>=0):
            temp = int(num2[len2]) + flag
            flag = temp // 2
            temp = temp % 2
            result += str(temp)
            len2 -= 1
        if(flag):
            result += '1'
        return result[::-1]



// not use // and %
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num1 = a
        num2 = b
        len1 = len(num1)-1
        len2 = len(num2)-1
        result = ''
        flag = 0
        while(len1>=0 and len2>=0):
            temp = flag
            flag = 0
            if num1[len1] == '1' and num2[len2] == '1':
                flag = 1
            elif (num1[len1] == '0' and num2[len2] == '0'):
                flag = 0
            else:
                flag = 0
                temp += 1
            if(temp == 2):
                flag = 1
                temp = 0
            result += str(temp)
            len1 -= 1
            len2 -= 1
        while(len1>=0):
            temp = flag
            flag = 0
            if num1[len1] == '1':
                temp += 1
            if(temp == 2):
                flag = 1
                temp = 0
            result += str(temp)
            len1 -= 1
        while(len2>=0):
            temp = flag
            flag = 0
            if num2[len2] == '1':
                temp += 1
            if(temp == 2):
                flag = 1
                temp = 0
            result += str(temp)
            len2 -= 1
        if(flag):
            result += '1'
        return result[::-1]
