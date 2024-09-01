# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        max = 0
        count = 1
        cur = root
        while cur.left!= None:
            count += 1
            cur = cur.left
        cur = root
        max = count
        count = 1
        while cur.right!= None:
            count += 1
            cur = cur.right
        if max > count:
            return max
        else:
            return count
            
