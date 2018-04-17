# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def travel(root):
            if root is not None:
                travel(root.left)
                l.append(root.val)
                travel(root.right)
                
        l = []
        travel(root)
        for i in range(len(l)-1):
            if l[i+1] <= l[i]:
                return False
        return True
        
