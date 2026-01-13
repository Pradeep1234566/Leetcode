# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root, ans):
            if root is None:
                return 0
            left_sum = max(0, self.helper(root.left, ans))
            right_sum = max(0, self.helper(root.right, ans))

            ans[0] = max(ans[0], root.val + left_sum + right_sum)

            return root.val + max(left_sum, right_sum)

    def maxPathSum(self, root):
        #your code goes here
        answer = [float('-inf')]
        self.helper(root, answer)
        return answer[0]