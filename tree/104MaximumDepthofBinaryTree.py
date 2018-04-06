# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def travel(root):
            if(root):
                return max(travel(root.left), travel(root.right))+1
            return 0
        
        return travel(root)
