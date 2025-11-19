class Solution(object):
    def isOneBitCharacter(self, bits):
        N = len(bits)
        i = 0

        while i < N - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1

        return i == N - 1
