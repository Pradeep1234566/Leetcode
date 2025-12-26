class Solution(object):

    def helper(self, index,  digits, mapping, result, temp):
        if index == len(digits):
            result.append(''.join(temp))
            return
        
        letters = mapping[digits[index]]

        for letter in letters:
            temp.append(letter)
            self.helper(index+1, digits, mapping, result, temp)
            temp.pop()
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
        }
        result = []
        temp = []
        index = 0
        if len(digits) == 0:
            return result

        self.helper(index,  digits, mapping, result, temp)
        return result
        

        