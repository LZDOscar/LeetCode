class Solution:
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 1
        cl = {}
        need = {}
        i = 0
        if len(nums) == 1:
            return False
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                count += 1
            else:
                cl[nums[i]] = count
                count = 1
            if nums[i] not in need:
                need[nums[i]] = 0
        cl[nums[i+1]] = count

        for inum in nums:
            if cl[inum] == 0:
                continue
            elif need[inum] > 0:
                need[inum] -= 1
                if inum+1 in need:
                    need[inum+1] += 1
                else:
                    need[inum+1] = 1

            elif inum+1 in cl and inum+2 in cl and cl[inum+1] > 0 and cl[inum+2] > 0:
                cl[inum+1] -= 1
                cl[inum+2] -= 1
                if inum+3 in need:
                    need[inum+3] += 1
                else:
                    need[inum+3] = 1
            else:
                return False
            cl[inum] -= 1
        return True
        
