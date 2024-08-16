class Solution(object):
    def isSubsequence(self, s, t):
        L1 = len(s)
        L2 = len(t)
        if s == '':
            return True
        elif L1 > L2:
            return False
        else:
            j = 0
            for i in range(L2):
                if t[i] == s[j]:
                    if j == L1 - 1:
                        return True
                    j = j +1
            