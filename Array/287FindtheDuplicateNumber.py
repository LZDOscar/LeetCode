//不修改数组，nlogn 主要是排序，不占用空间
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left, right = 0, len(nums)-1
        while(left < right):
            print(left, right)
            if(nums[left] == nums[right]):
                 return nums[left]
            mid = (left+right)//2
            if(mid+1 == nums[mid]):
                left = mid 
            if(mid+1 > nums[mid]):
                right = mid 
            if(mid+1 < nums[mid]):
                left = mid  
        return None


//可修改数组，不需要排序，n,不占用空间， 思路：遍历一遍，把对应的数置负，第二次遇见一个数，此对应数为负，可判断。
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for n in nums:
            if n < 0:
                i = -n
            else:
                i = n
            ind = i - 1
            if nums[ind] < 0:
                return i
            else:
                
                nums[ind] = -nums[ind]
        

        return extra


//占用空间，不修改数组
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter 
        c = Counter(nums)
        for i, v in c.items():
            if v > 1:
                return i
