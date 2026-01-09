class Solution(object):
    def helper(self, root):
        if root is None:
            return 0, None   # height, node
        
        lh, ln = self.helper(root.left)
        rh, rn = self.helper(root.right)

        if lh > rh:
            return lh + 1, ln
        elif rh > lh:
            return rh + 1, rn
        else:
            return lh + 1, root   

    def subtreeWithAllDeepest(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        return self.helper(root)[1]
