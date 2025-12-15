class Solution(object):
    def helper(self, root, val):
        if root is None:
            return TreeNode(val)

        if val >= root.val:
            root.right = self.helper(root.right, val)
        else:
            root.left = self.helper(root.left, val)

        return root

    def insertIntoBST(self, root, val):
        return self.helper(root, val)
