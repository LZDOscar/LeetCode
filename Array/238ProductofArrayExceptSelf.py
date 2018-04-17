class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        last = 1
        if(len(nums) == 0):
            return 0
        if(len(nums) == 1):
            return nums[0]
        sum = 1
        zero = []
        for i in range(0,len(nums)):
            if(nums[i] == 0):
                zero.append(i)
                continue
            sum *= nums[i]
        if(len(zero)>=2):
            return [0]*len(nums)
        elif(len(zero)>=1):
            temp = [0]*len(nums)
            temp[zero[0]] = sum
            return temp
        else:
            i = 0
            while(i < len(nums)):
                nums[i] = int(sum / nums[i])
                i += 1
            return nums
            
            
