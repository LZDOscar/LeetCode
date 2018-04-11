// 递归回溯
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []   
        self.count = 0
        self.around = 0
        def DFS(start, nums):
            if self.count == k:
                ans.append(nums)
                # print(nums)
                self.around += 1
                # print(self.around)
                return 
            
            for i in range(start, n+1):
                self.count += 1
                # print(nums+[i])
                DFS(i+1, nums+[i])
                self.count -= 1
        
        DFS(1,[])
        
        return ans

//dp
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return [[]]
        if k == n:
            return [[i for i in range(1, n+1)]]
        ans1 = self.combine(n - 1, k)
        ans2 = self.combine(n - 1, k - 1)
        for a in ans2:
            a.append(n)
            ans1.append(a)
        return ans1
                
            
            
