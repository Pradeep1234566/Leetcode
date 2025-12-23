class Solution(object):
    def helper(self, start, end):
        if start > end:
            return [None]

        trees = []  # ✅ local list for this range

        for i in range(start, end + 1):
            left_subtrees = self.helper(start, i - 1)
            right_subtrees = self.helper(i + 1, end)

            for left in left_subtrees:
                for right in right_subtrees:
                    node = TreeNode(i)
                    node.left = left
                    node.right = right
                    trees.append(node)

        return trees  # ✅ return list, not node

    def generateTrees(self, n):
        if n == 0:
            return []
        return self.helper(1, n)
