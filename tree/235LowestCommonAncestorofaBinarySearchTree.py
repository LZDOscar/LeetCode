# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if (p==q):
            return p
        imin = min(p.val, q.val)
        imax = max(p.val, q.val)
        while(root):
            if(root.val >= imin and root.val <= imax):
                return root
            if(root.val > imax):
                root = root.left
            if(root.val < imin):
                root = root.right
        return root
