# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, result, temp, root, targetSum):
        if root is None:
            return 
        
        temp.append(root.val)

        if root.left is None and root.right is None:
            if targetSum == root.val:
                result.append(temp[:])
        
        else:
            self.helper(result, temp, root.left, targetSum-root.val)
            self.helper(result, temp, root.right, targetSum-root.val)

        temp.pop()

    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []
        temp = []
        self.helper(result, temp, root, targetSum)
        return result
        
        