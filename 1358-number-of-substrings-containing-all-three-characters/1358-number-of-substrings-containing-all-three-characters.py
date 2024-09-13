class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        N = len(s)
        count = {'a' : 0, 'b' : 0, 'c' : 0}
        total = 0
        while right < N:
            count[s[right]] += 1
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                total += len(s) - right
                count[s[left]] -= 1
                left += 1
            right += 1
        return total
        