class Solution(object):
    def check(self, root, maximum):
        if root is None:
            return 0
        
        # A node is good if its value >= maximum so far
        good = 1 if root.val >= maximum else 0

        # Update the maximum for the next path
        new_max = max(maximum, root.val)

        # Recursively count good nodes in left and right
        left_good = self.check(root.left, new_max)
        right_good = self.check(root.right, new_max)

        return good + left_good + right_good

    def goodNodes(self, root):
        return self.check(root, root.val)
