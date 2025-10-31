class Solution(object):
    def helper(self, root, result, path):
        if root is None:
            return

        path += str(root.val)

        # If it's a leaf, store the path
        if root.left is None and root.right is None:
            result.append(path)
            return

        # Add arrow only if there are more nodes ahead
        path += "->"
        self.helper(root.left, result, path)
        self.helper(root.right, result, path)

    def binaryTreePaths(self, root):
        result = []
        self.helper(root, result, "")
        return result
