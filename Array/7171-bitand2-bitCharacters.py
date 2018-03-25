//forward
class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        l = len(bits)
        count = 0
        i = 0
        while(i<l-1):
            if(bits[i] == 0):
                i += 1
            else:
                i += 2
        if(i == l-1):
            return True
        else:
            return False



//backward, 只需要看倒数第二个是否是0，如果是0 必然true, 如果是1，那就再往前看有多少个连续的1，如果是偶数个，则是true，奇数个是false, 整个思路的前提是输入字符串必须合法。
class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = len(bits)-1
        count = 0
        while(i>=1 and bits[i-1]):
            count += 1
            i -= 1
        if(count % 2 == 0):
            return True
        else:
            return False
