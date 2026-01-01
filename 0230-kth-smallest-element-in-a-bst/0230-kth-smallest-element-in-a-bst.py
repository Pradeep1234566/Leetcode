# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.k = k
        self.answer = None

        def helper(root):
            if not root or self.answer is not None:
                return 
            
            helper(root.left)

            self.k -= 1
            if self.k == 0:
                self.answer = root.val
                return 
            
            helper(root.right)
        
        helper(root)
        return self.answer


        