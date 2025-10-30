class Solution(object):
    def check(self, root):
        if root is None:
            return 0  # height = 0

        left_height = self.check(root.left)
        if left_height == -1:  # left subtree not balanced
            return -1

        right_height = self.check(root.right)
        if right_height == -1:  # right subtree not balanced
            return -1

        # If current node is unbalanced
        if abs(left_height - right_height) > 1:
            return -1

        # Return height if balanced
        return 1 + max(left_height, right_height)

    def isBalanced(self, root):
        return self.check(root) != -1
