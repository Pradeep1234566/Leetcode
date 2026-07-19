# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def print_tree(self, root, result, row, column, height):
        if root is None:
            return

        result[row][column] = str(root.val)

        if root.left:
            self.print_tree(
                root.left,
                result,
                row + 1,
                column - (2 ** (height - row - 1)),
                height
            )

        if root.right:
            self.print_tree(
                root.right,
                result,
                row + 1,
                column + (2 ** (height - row - 1)),
                height
            )

    def get_height(self, root):
        if root is None:
            return -1         

        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)

        return 1 + max(left_height, right_height)

    def printTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[str]]
        """

        ht = self.get_height(root)

        rows = ht + 1
        columns = (2 ** (ht + 1)) - 1

        result = [["" for _ in range(columns)] for _ in range(rows)]

        self.print_tree(root, result, 0, (columns - 1) // 2, ht)

        return result