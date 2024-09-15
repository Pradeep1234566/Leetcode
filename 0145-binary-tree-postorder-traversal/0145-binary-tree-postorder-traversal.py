# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        answer = []
        answer += self.postorderTraversal(root.left)
        answer += self.postorderTraversal(root.right)
        answer.append(root.val)
        return answer
        