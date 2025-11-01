# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maximum = float('-inf')
        def helper(root):

            if root is None:
                return 0
        
            left = max(0, helper(root.left))
            right = max(0, helper(root.right))

            path_sum = left + right + root.val

            self.maximum = max(self.maximum, path_sum)

            return root.val + max(left, right)
        
        helper(root)
        return self.maximum

        
        