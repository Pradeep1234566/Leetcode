class Solution(object):
    def helper(self, root, traversal):
        if root is None:
            return
        
        self.helper(root.left, traversal)
        traversal.append(root.val)
        self.helper(root.right, traversal)
        
    def isValidBST(self, root):
        traversal = []
        self.helper(root, traversal)

        for i in range(1, len(traversal)):
            if traversal[i] <= traversal[i - 1]:
                return False

        return True
