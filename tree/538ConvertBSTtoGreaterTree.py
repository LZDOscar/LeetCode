# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    sum = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def  tavel(root,):
            if(root):
                tavel(root.right)
                self.sum += root.val
                root.val = self.sum
                tavel(root.left)
            else:
                return 
        
        tavel(root)
        return root
                
