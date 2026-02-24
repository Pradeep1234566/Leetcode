# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, root, current):
        if root is None:
            return 0
        
        current = (current<<1) | root.val

        if root.left is None and root.right is None:
            return current

        
        return self.dfs(root.left, current) + self.dfs(root.right, current)


    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        current = 0
        return self.dfs(root, current)

        