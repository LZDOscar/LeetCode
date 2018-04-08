# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        def create(nums, sta, end):
            if(sta > end):
                return None
            mid = (end + sta +1 )//2
            root = TreeNode(nums[mid])
            root.left = create(nums, sta, mid-1)
            root.right = create(nums, mid+1, end)
            return root
       
        if(len(nums) == 0 ):
            return None
        Len = len(nums)
        root = create(nums, 0, Len-1)
        
        return root
        
