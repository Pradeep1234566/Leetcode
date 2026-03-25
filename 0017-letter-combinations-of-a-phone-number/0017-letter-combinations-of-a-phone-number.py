class Solution(object):
    def helper(self, index, digits, mapping, temp, result):
        if index == len(digits):
            result.append(temp)
            return

        letters = mapping[digits[index]]

        for letter in letters:
            self.helper(index + 1, digits, mapping, temp + letter, result)

    def letterCombinations(self, digits):
       mapping = {
        '2' : 'abc',
        '3' : 'def',
        '4' : 'ghi',
        '5' : 'jkl',
        '6' : 'mno',
        '7' : 'pqrs',
        '8' : 'tuv',
        '9' : 'wxyz'
       }
       temp = []
       result = []
       index = 0
       self.helper(index, digits, mapping, '', result)
       return result

       