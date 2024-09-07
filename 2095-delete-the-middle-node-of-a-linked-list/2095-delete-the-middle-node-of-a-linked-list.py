# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        i = 0
        cur = head
        prev = None
        n = count // 2
        if n == 0:
            return head
        while i < n:
            prev = cur
            cur = cur.next
            i += 1
        prev.next = cur.next
        return head
        
        