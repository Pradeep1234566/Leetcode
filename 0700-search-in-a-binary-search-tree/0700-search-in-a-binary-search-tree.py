# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        cur = root
        if cur is None:
            return None
        if cur.val == val:
            return cur
        elif cur.val > val:
            return self.searchBST(cur.left, val)  # return the result of the recursive call
        else:
            return self.searchBST(cur.right, val)  # return the result of the recursive call

        
        