class Solution(object):
    def helper(self, root, frequency):
        if root is None:
            return 
        
        if root.val not in frequency:
            frequency[root.val] = 1
        else:
            frequency[root.val] += 1
        
        self.helper(root.left, frequency)
        self.helper(root.right, frequency)

    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        frequency = {}
        self.helper(root, frequency)
        
        max_freq = max(frequency.values())
        result = []
        
        for key, value in frequency.items():
            if value == max_freq:
                result.append(key)
        
        return result
