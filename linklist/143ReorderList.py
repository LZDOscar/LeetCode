# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        Len = 0
        node = head
        last = head
        while(node):
            Len += 1
            last = node
            node = node.next
        if(Len >= 2):
            mid = (Len+1)//2
            midnode = head
            pre = None
            while(mid):
                mid -= 1
                pre = midnode
                midnode = midnode.next

            pre.next = None
            pre = None

            while(midnode):
                cur = midnode.next
                midnode.next = pre
                pre  = midnode
                midnode = cur

            node = head
            lnode = last

            while(last):
                curhead = node.next
                curlast = last.next
                node.next = last
                last.next = curhead
                node = node.next.next
                last = curlast


            while(head):
                print(head.val)
                head = head.next
        # return head
            
