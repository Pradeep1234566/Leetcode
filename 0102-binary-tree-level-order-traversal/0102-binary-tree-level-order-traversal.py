# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        queue = []
        queue.append(root)
        
        while queue:
            size = len(queue)
            level = []

            for i in range(size):
                temp = queue.pop(0)

                level.append(temp.val)

                if temp.left:
                    queue.append(temp.left)
                
                if temp.right:
                    queue.append(temp.right)
            
            result.append(level)
        return result
        

        