class Solution(object):
    def check(self, root):
        if root is None:
            return 0
        
        left_height = self.check(root.left)
        right_height = self.check(root.right)

        if left_height == -1 or right_height == -1:
            return -1

        difference = abs(left_height - right_height)
        if difference > 1:
            return -1

        return 1 + max(left_height, right_height)

    def isBalanced(self, root):
        return self.check(root) != -1
    
        

