class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left = 0
        right = 0
        t_map = {}
        N = len(s)
        M = len(t)
        count = 0
        starting_index = -1
        min_length = float('inf')

        # Initialize frequency map for t
        for i in t:
            if i not in t_map:
                t_map[i] = 1
            else:
                t_map[i] += 1

        while right < N:
            if s[right] in t_map:
                t_map[s[right]] -= 1
                if t_map[s[right]] >= 0:
                    count += 1

            while count == M:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    starting_index = left

                if s[left] in t_map:
                    if t_map[s[left]] >= 0:
                        count -= 1
                    t_map[s[left]] += 1

                left += 1

            right += 1

        if starting_index == -1:
            return ""
        else:
            return s[starting_index:starting_index + min_length]
