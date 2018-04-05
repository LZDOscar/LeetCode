# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ssum = 0
        def Sum(root):
            if(root == None):
                return 0
            left = Sum(root.left)
            right = Sum(root.right)
            self.ssum += abs(left-right)
            return left+right+root.val
           
        
        Sum(root)
        return self.ssum
