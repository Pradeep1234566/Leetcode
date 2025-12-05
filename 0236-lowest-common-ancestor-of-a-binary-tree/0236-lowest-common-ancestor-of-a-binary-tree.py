class Solution(object):
    def get_path(self, node, p, q):
        if node is None or node == p or node == q:
            return node

        left = self.get_path(node.left, p, q)
        right = self.get_path(node.right, p, q)

        if left is None:
            return right
        
        elif right is None:
            return left
        
        else:
            return node
        

    def lowestCommonAncestor(self, root, p, q):
        return self.get_path(root, p, q)
