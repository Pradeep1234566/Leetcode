# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root):
        if root is None:
            return 0
        
        left_height = 1 + self.helper(root.left)
        right_height = 1 + self.helper(root.right)

        return max(left_height, right_height)

    def maxDepth(self, root):
        #your code goes here
        return self.helper(root)
