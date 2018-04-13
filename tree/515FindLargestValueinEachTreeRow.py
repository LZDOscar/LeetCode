# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        Max = []
        node = [root]
        while any(node):
            Max.append(max(i.val for i in node))
            node = [kid for i in node for kid in (i.left, i.right) if kid]
        return Max
