class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        self.count = 0
        def travel(t1, t2):
            if not t1 and not t2:
                return None
            
            root = TreeNode(0) 
            if t1 and t2:
                root.val = t1.val + t2.val
                root.left = travel(t1.left, t2.left)
                root.right = travel(t1.right, t2.right)
                
            elif t1:
                root.val = t1.val
           
                root.left = travel(t1.left, None)
                root.right = travel(t1.right, None)
            elif t2:
                root.val = t2.val
         
                root.left = travel(None, t2.left)
                root.right = travel(None, t2.right)
                
            return root
         

            
            
     
        root = travel(t1,t2)
        return root
