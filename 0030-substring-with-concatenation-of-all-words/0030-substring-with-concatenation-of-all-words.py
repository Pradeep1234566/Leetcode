class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        from collections import Counter

        word_len = len(words[0])
        total_words = len(words)
        window_len = word_len * total_words
        n = len(s)

        word_freq = Counter(words)
        result = []

        for offset in range(word_len):
            left = offset
            right = offset
            seen = Counter()
            count = 0

            while right + word_len <= n:
                word = s[right:right + word_len]
                right += word_len

                if word in word_freq:
                    seen[word] += 1
                    count += 1

                    while seen[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    # Valid window
                    if count == total_words:
                        result.append(left)

                else:
                    # Reset window
                    seen.clear()
                    count = 0
                    left = right

        return result
