from collections import deque    

class Solution(object):
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        
        queue = deque([root])   # FIXED
        result = []
        count = 0

        while queue:
            level = []
            size = len(queue)
            for i in range(size):
                temp = queue.popleft()
                level.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)

            if count % 2 != 0:  
                level = level[::-1]
            
            result.append(level)
            count += 1           

        return result
