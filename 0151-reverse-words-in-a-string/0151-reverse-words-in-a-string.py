class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Split the string into words based on whitespace, and remove extra spaces
        words = s.split()
        # Reverse the list of words
        reversed_words = words[::-1]
        print(reversed_words)
        # Join the reversed words with a single space and return
        return " ".join(reversed_words)
