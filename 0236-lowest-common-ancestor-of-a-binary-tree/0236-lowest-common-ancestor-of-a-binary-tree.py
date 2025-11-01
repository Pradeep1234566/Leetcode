class Solution(object):
    def get_path(self, node, val, path):
        if node is None:
            return False

        path.append(node)

        if node == val:
            return True

        if self.get_path(node.left, val, path) or self.get_path(node.right, val, path):
            return True

        path.pop()
        return False

    def lowestCommonAncestor(self, root, p, q):
        path1 = []
        path2 = []

        self.get_path(root, p, path1)
        self.get_path(root, q, path2)

        i = 0
        while i < len(path1) and i < len(path2) and path1[i] == path2[i]:
            i += 1

        return path1[i - 1]
