# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        # Two pointers
        pointerA, pointerB = headA, headB
        
        # Traverse both lists
        while pointerA != pointerB:
            # If pointerA reaches the end of listA, move it to headB
            pointerA = pointerA.next if pointerA else headB
            # If pointerB reaches the end of listB, move it to headA
            pointerB = pointerB.next if pointerB else headA
        
        # If they intersect, both will eventually point to the intersection node.
        # Otherwise, they will both become None after the second traversal.
        return pointerA
