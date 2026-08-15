# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def helper(self, preorder, inorder, start, end, preorderindex):
        if start > end:
            return 
        
        temp = preorder[preorderindex[0]]
        

        root = TreeNode(temp)
        preorderindex[0] += 1

        for i in range(len(inorder)):
            if root.val == inorder[i]:
                idx = i
                break

        root.left = self.helper(preorder, inorder, start, idx-1, preorderindex)
        
        root.right = self.helper(preorder, inorder, idx+1, end, preorderindex)

        return root

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        start = 0
        end = len(preorder)-1
        preorderindex = [0]

        return self.helper(preorder, inorder, start, end, preorderindex)
        