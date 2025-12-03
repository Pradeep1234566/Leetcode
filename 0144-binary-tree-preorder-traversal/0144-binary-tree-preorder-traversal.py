class Solution(object):

    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        return self.helper(root, [])

    def helper(self, root, answer):
        if root is None:
            return answer
        
        answer.append(root.val)
        self.helper(root.left, answer)
        self.helper(root.right, answer)

        return answer
