# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node to serve as the starting point of the merged list
        dummy = ListNode()
        current = dummy
        
        # Iterate while both lists are not empty
        while list1 and list2:
            if list1.val < list2.val:
                # Append list1's node to the merged list
                current.next = list1
                list1 = list1.next
            else:
                # Append list2's node to the merged list
                current.next = list2
                list2 = list2.next
            # Move the current pointer forward
            current = current.next
        
        # If there are remaining nodes in list1 or list2, append them
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        # The merged list starts from dummy.next
        return dummy.next
