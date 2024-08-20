class Solution(object):
    def isAnagram(self, s, t):
        k = len(s)
        m = len(t)
        counter = {}
        if k == m:
            for i in s:
                if i not in counter:
                    counter[i] = 1
                else:
                    counter[i] += 1
            for i in t:
                if i not in counter:
                    return False
                elif counter[i] == 1:
                    del counter[i]
                else:
                    counter[i] -= 1
            return True
        else:
            return False
