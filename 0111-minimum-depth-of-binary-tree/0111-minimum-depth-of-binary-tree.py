class Solution(object):
    def helper(self, root):
        if root is None:
            return float('inf')  # important trick

        # leaf node
        if root.left is None and root.right is None:
            return 1

        return 1 + min(
            self.helper(root.left),
            self.helper(root.right)
        )

    def minDepth(self, root):
        if root is None:
            return 0
        return self.helper(root)
