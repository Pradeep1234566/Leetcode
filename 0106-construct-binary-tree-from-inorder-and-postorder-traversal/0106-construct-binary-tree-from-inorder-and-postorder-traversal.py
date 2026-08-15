# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def helper(self, postorder, inorder, start, end, postorderindex):
        if start > end:
            return 

        temp = postorder[postorderindex[0]]
        postorderindex[0] -= 1

        root = TreeNode(temp)

        for i in range(len(postorder)):
            if inorder[i] == temp:
                idx = i
                break

        root.right = self.helper(postorder, inorder, idx+1, end, postorderindex)
        root.left = self.helper(postorder, inorder, start, idx-1, postorderindex)

        return root


    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        start = 0
        end = len(postorder) - 1
        postorderindex = [len(postorder)-1]
        return self.helper(postorder, inorder, start, end, postorderindex)


        