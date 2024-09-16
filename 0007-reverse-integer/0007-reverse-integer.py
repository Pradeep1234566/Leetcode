class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        answer = []
        key = 0
        if x < 0:
            key = 1
            x = abs(x)
        while x:
            answer.append(x%10)
            x = x // 10
        answer.reverse()
        # print(answer)
        total = 0
        for i in range(len(answer)):
            k = (10**i) * answer[i]
            total += k
        # print(total)
        if total < -2**31 or total > 2**31 - 1:
            return 0
        if key == 1:
            return (-1) * total
        else:
            return total
