from collections import deque

class Solution(object):
    def widthOfBinaryTree(self, root):
        if not root:
            return 0

        queue = deque([(root, 0)])  # store (node, index)
        maximum = 0

        while queue:
            size = len(queue)
            _, first = queue[0]  # leftmost index
            _, last = queue[-1]  # rightmost index
            maximum = max(maximum, last - first + 1)

            for _ in range(size):
                node, index = queue.popleft()

                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))
        
        return maximum
