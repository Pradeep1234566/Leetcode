class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        # Frequency map to store the max required frequency for each character in words2
        freq = {}
        
        # Update freq with the max count of each character across words2
        for word in words2:
            word_freq = {}
            for char in word:
                word_freq[char] = word_freq.get(char, 0) + 1
            
            # For each character, we store the maximum count across all words in words2
            for char, count in word_freq.items():
                freq[char] = max(freq.get(char, 0), count)
        
        print(freq)  # Check the frequency map for words2
        
        # Now check each word in words1 to see if it satisfies the universal condition
        result = []
        for word in words1:
            word_freq = {}
            for char in word:
                word_freq[char] = word_freq.get(char, 0) + 1
            
            # Check if word contains all characters in the frequency map with the required multiplicity
            if all(word_freq.get(char, 0) >= freq[char] for char in freq):
                result.append(word)

        return result
