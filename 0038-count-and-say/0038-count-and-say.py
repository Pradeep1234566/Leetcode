class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        answer = []
        if n == 1:
            return '1'
        k = self.countAndSay(n-1)
        print(k)
        count = 1
        for i in range(1, len(k)):
            if k[i] == k[i-1]:
                count += 1
            else:
                answer.append(str(count))
                answer.append(k[i-1])
                count = 1
        answer.append(str(count))
        answer.append(k[-1])
        return ''.join(answer)