# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        # Dummy node to handle cases where head needs to be removed
        dummy = ListNode(0)
        dummy.next = head
        prev, cur = dummy, head

        while cur:
            if cur.val == val:
                prev.next = cur.next  # Remove current node
            else:
                prev = cur  # Move prev only if cur is not removed
            cur = cur.next  # Move to the next node
        
        return dummy.next  # New head
