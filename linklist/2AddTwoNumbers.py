# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flag = 0
        root = ListNode(l1.val + l2.val)
        l1 = l1.next
        l2 = l2.next
        node = root
        while(l1 and l2):
            node.next = ListNode(l1.val + l2.val)
            node = node.next
            l1 = l1.next
            l2 = l2.next
        while(l1):
            node.next = l1
            l1 = l1.next
            node = node.next
        while(l2):
            node.next = l2
            l2 = l2.next
            node = node.next
        
        
        cur = root
        last = cur

        while(cur):
            cur.val = cur.val + flag
            if(cur.val >= 10):
                cur.val -= 10
                flag = 1
            else:
                flag = 0
            last = cur
            cur = cur.next
        if flag == 1:
            last.next = ListNode(1)
        return root
            
            
            
