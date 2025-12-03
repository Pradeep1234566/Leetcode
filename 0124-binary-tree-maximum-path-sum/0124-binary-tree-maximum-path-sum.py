class Solution(object):
    def helper(self, root, answer):
        if root is None:
            return 0
        
        # if the value goes less than zero we drop that
        left_sum = max(0, self.helper(root.left, answer))
        right_sum = max(0, self.helper(root.right, answer))

        # max path through current node
        total_sum = root.val + left_sum + right_sum
        answer[0] = max(answer[0], total_sum)

        # return best path going UP
        return root.val + max(left_sum, right_sum)

    def maxPathSum(self, root):
        answer = [float('-inf')]
        self.helper(root, answer)
        return answer[0]
