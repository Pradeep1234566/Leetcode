# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def find_successor(self, root):
        while root.left:
            root = root.left

        return root

    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        else:

            if not root.left:
                return root.right

            
            if not root.right:
                return root.left
            

            successor = self.find_successor(root.right)
            root.val = successor.val

            root.right = self.deleteNode(root.right, successor.val)
        
        return root


        