class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        Find = {}
        Need = {}
        for c in t:
            if c not in Need:
                Need[c] = 1
            else:
                Need[c] += 1
        for c in s:
            Find[c] = 0
        minstart = 0
        minend = 0
        start = 0
        end = 0
        minsize = len(s)+1
        count = len(t)
        
        Find[s[0]] = 1
        if s[0] in Need and Need[s[0]] >= Find[s[0]]:
            count -= 1
        while(True):
            if count == 0:       
                while(s[start] not in Need or Need[s[start]] < Find[s[start]]):
                  
                    Find[s[start]] -= 1
                    start += 1
                if(end - start + 1 < minsize):
                    minstart = start
                    minend = end
                    minsize = end - start +1
         
            if end < len(s)-1:
                end += 1
                Find[s[end]] += 1
                if s[end] in Need and Need[s[end]] >= Find[s[end]]:
                    count -= 1
            else:
                break
        if(minsize < len(s)+1):
            return s[minstart:minend+1]
        else:
            return ""
        
        
