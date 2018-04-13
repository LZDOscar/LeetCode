//效率奇差无比。。原因在于deepcopy, 浅拷贝copy在这题就可以，不需要深拷贝，
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        import copy
        Map = {}
        for i in p:
            if i in Map:
                Map[i] += 1
            else:
                Map[i] = 1
        curMap = copy.deepcopy(Map)
        left, right = 0, 0
        res = []
        count = 0
        while(right <= len(s)-1):
            if count < len(p):
                if s[right] in curMap and curMap[s[right]] != 0:
                    count += 1
                    curMap[s[right]] -= 1
                    
                elif s[right] not in curMap:
                    left = right + 1
                    curMap = copy.deepcopy(Map)
                    count = 0
                elif s[right] == s[left]:
                    left += 1
                else:
                    left = right
                    count = 1
                    curMap = copy.deepcopy(Map)
                    curMap[s[right] ] -= 1
            if count == len(p):
                res.append(left)
                curMap[s[left]] += 1
                left += 1
                count -= 1
                
            right += 1
        return res
        
