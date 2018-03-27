//the version of myself
class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sta = nums[0]*nums[1]*nums[-1]
        end = nums[-2]*nums[-3]*nums[-1]
        return max(sta,end)


//not use sort 
class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg1 = 1000
        neg2 = 1000
        pos1 = -1000
        pos2 = -1000
        pos3 = -1000
        for i in nums:
            if i < neg1:
                neg2 = neg1
                neg1 = i
            elif i < neg2:
                neg2 = i

            if i > pos1:
                pos3 = pos2
                pos2 = pos1
                pos1 = i
            elif i > pos2:
                pos3 = pos2
                pos2 = i
            elif i > pos3:
                pos3 = i
            
                    
        return max(neg1 * neg2 * pos1, pos1 * pos2 * pos3)


//fast use heapq 无耻的调用了模块
class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(a[0]*a[1]*a[2], a[0]*b[0]*b[1])

