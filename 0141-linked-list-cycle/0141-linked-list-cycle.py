# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        current = head
        seen_nodes = set()  # Use a set to store node references
        while current:
            if current in seen_nodes:
                return True  # Cycle detected
            seen_nodes.add(current)
            current = current.next
        return False  # No cycle
