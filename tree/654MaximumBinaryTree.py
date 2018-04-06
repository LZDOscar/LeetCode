# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def construct(nums):
            if(len(nums) == 0):
                return None
            Max = max(nums)
            Index = nums.index(Max)
            node = TreeNode(Max)
            node.left = construct(nums[:Index])
            node.right = construct(nums[Index+1:])
            return node
        root = construct(nums)
        return root
