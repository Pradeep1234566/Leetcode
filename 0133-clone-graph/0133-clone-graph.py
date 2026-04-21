"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None
        
        queue = deque()
        queue.append(node)
        cloned = {}
        cloned[node] = Node(node.val)

        while queue:
            current = queue.popleft()
            for neighbour in current.neighbors:
                if neighbour not in cloned:
                    cloned[neighbour] = Node(neighbour.val)
                    queue.append(neighbour)
                
                cloned[current].neighbors.append(cloned[neighbour])
        
        return cloned[node]


