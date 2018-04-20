class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = {}
        for i in s:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        l = list(map(lambda x,y: (x,y), count.keys(),count.values()))
        
        l.sort(key=lambda k: k[1], reverse=True)
        # print (l)
        s = ''
        for i in l:
            s += i[1]*i[0]
        return s
        
