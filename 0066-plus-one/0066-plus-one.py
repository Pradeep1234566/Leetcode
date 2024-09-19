class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        k = 0
        n = len(digits)
        for i in range(n):
            m = digits[i] * (10**(n-i-1))
            #print(m)  # This will print each intermediate result
            k += m
        #print(k)  # This will print the final number
        k = k + 1
        answer = []
        print(k)
        while(k):
            answer.append(k%10)
            k = k / 10
        answer.reverse()
        return answer



        