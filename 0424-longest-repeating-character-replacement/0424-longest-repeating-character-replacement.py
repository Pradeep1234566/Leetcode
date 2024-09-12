class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        right = 0
        n = len(s)
        max_length = 0
        freq = {}
        max_freq = 0  # Tracks the highest frequency of any character in the current window

        while right < n:
            # Update the frequency of the current character
            if s[right] not in freq:
                freq[s[right]] = 1
            else:
                freq[s[right]] += 1

            # Update the max frequency character in the window
            max_freq = max(max_freq, freq[s[right]])

            length = right - left + 1  # Current window size
            
            # If the number of characters to replace exceeds k, shrink the window
            if length - max_freq > k:
                freq[s[left]] -= 1
                left += 1  # Shrink the window from the left

            # Update the maximum valid window length
            max_length = max(max_length, right - left + 1)
            
            right += 1

        return max_length
