class Solution(object):
    def helper(self, index, digits, mapping, result, curr):
        if index == len(digits):
            result.append(curr)
            return

        letters = mapping[digits[index]]
        for letter in letters:
            self.helper(index + 1, digits, mapping, result, curr + letter)

    def letterCombinations(self, digits):
        if not digits:
            return []

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
        self.helper(0, digits, mapping, result, "")
        return result
