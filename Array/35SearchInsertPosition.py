class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sta = 0
        end = len(nums)-1
        while(sta <= end):
            mid = (end+sta)//2
            if(nums[mid] == target):
                return mid
            elif(nums[mid] > target):
                end = mid-1
            else:
                sta = mid+1
        return sta
