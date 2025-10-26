class Solution(object):
    def helper(self, s):
        return s == s[::-1]
    
    def get_solution(self, s, index, temp, result):
        if index == len(s):
            result.append(temp[:])
            return 
        
        for j in range(index, len(s)):
            substring = s[index:j+1]
            if self.helper(substring):
                temp.append(substring)
                self.get_solution(s, j+1, temp, result)
                temp.pop()
            
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        result = []
        temp = []
        self.get_solution(s, 0, temp, result)
        return result

        