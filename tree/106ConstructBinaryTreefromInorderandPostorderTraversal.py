# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def build(inorder, postorder):
            if(len(inorder) == 0):
                return None
            val = postorder[-1]
            for i,v in enumerate(inorder):
                if v == val:
                    break
            
            root = TreeNode(val)
            root.left = build(inorder[:i], postorder[:i])
            root.right = build(inorder[i+1:], postorder[i:-1])
            return root
        
        root = build(inorder, postorder)
        return root
