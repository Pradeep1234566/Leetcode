class Solution(object):
    def helper(self, root, answer):
        if root is None:
            return 0    # height is 0
        
        left_height = self.helper(root.left, answer)
        right_height = self.helper(root.right, answer)

        # update diameter
        answer[0] = max(answer[0], left_height + right_height)

        # return height
        return 1 + max(left_height, right_height)

    def diameterOfBinaryTree(self, root):
        answer = [0]       # store diameter
        self.helper(root, answer)
        return answer[0]
