# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        current = head
        count = 0
        while(current):
            count += 1
            current = current.next
        print(count)
        # if count % 2 == 0:
        #     n = int(count/2) 
        # else:
        #     n = int(count/2)
        n = count/2
        i = 0
        print(n)

        while(i<n):
            head = head.next
            i += 1
        return head
        