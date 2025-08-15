# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxi = 0
        def height(root):
            if root is None:
                return 0
        
            left_height = height(root.left)
            right_height = height(root.right)

            self.maxi = max(self.maxi, left_height + right_height)

            return 1 + max(left_height, right_height)
        
        height(root)
        return self.maxi