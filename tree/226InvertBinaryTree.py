# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def travel(root):
            if(root):
                root.left, root.right = root.right, root.left
                travel(root.left)
                travel(root.right)

        travel(root)
        
        return root
