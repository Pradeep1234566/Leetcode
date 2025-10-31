class Solution(object):
    def helper(self, root, total):
        if not root:
            return 0

        left_sum = self.helper(root.left, total)
        right_sum = self.helper(root.right, total)

        total[0] += abs(left_sum - right_sum)
        return root.val + left_sum + right_sum

    def findTilt(self, root):
        total = [0]   # list used as a mutable container
        self.helper(root, total)
        return total[0]
