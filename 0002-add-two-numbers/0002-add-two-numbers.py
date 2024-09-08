# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)  # Dummy node to simplify result creation
        cur = dummy  # Pointer to build the result list
        cur1 = l1
        cur2 = l2
        k = 0  # Carry variable
        
        while cur1 or cur2 or k:  # Continue while there are nodes or carry
            val1 = cur1.val if cur1 else 0  # Get value from cur1 if exists, otherwise 0
            val2 = cur2.val if cur2 else 0  # Get value from cur2 if exists, otherwise 0
            
            total = val1 + val2 + k  # Sum the values and carry
            k = total // 10  # Calculate new carry
            cur.next = ListNode(total % 10)  # Store the current digit (mod 10)
            
            cur = cur.next  # Move to the next node in the result list
            
            if cur1:
                cur1 = cur1.next  # Move to the next node in cur1
            if cur2:
                cur2 = cur2.next  # Move to the next node in cur2
        
        return dummy.next  # Return the head of the result linked list

