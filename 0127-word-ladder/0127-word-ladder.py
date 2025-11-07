from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        temp = set(wordList)

        if endWord not in temp:
            return 0
        traversal = 'abcdefghijklmnopqrstuvwxyz'
        queue = deque([(beginWord, 1)])
        
        
        while queue:
            word, level = queue.popleft()
            for i in range(len(word)):
                original = word[i]
                for ch in traversal:
                    newword = word[:i] + ch + word[i+1:]
                    if ch == original:
                        continue

                    if newword == endWord:
                        return level + 1

                    if newword in temp:
                        temp.remove(newword)
                        queue.append((newword,level+1))
        
        return 0



        