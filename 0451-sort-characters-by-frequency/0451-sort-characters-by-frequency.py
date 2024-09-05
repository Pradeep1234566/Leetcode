class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = sorted(s)  # This will sort the string, but you might not need it here
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 1  # Initialize the count to 1
            else:
                freq[i] += 1  # Increment the count
        
        # Sort the dictionary by frequency in descending order
        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        print(sorted_chars)
        # Build the output string
        result = ''.join([char * count for char, count in sorted_chars])
        
        return result
