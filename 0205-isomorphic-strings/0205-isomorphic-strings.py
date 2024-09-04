class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map = {}
        map2 = {}
        
        for i, j in zip(s, t):
            if i not in map:
                map[i] = j
            else:
                k = map[i]
                if k != j:
                    return False
            
            if j not in map2:
                map2[j] = i
            else:
                a = map2[j]
                if a != i:
                    return False
        
        return True
