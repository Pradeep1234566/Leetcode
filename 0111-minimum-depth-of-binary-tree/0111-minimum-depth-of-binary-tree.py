# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, root):
        if root is None:
            return 0
        
        if root.left is None:
            return 1 + self.helper(root.right)
        
        if root.right is None:
            return 1 + self.helper(root.left)

        
        return 1 + min(self.helper(root.right), self.helper(root.left))
        
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return self.helper(root)
        