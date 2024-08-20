class Solution(object):
    def maxNumberOfBalloons(self, text):
        counter = {}
        for i in text:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1
        counter['l'] =int(counter.get('l', 0) // 2)
        counter['o'] = int(counter.get('o', 0) // 2)
        print(counter)
        return min(counter.get('b', 0),counter.get('a', 0),counter.get('l', 0),counter.get('o', 0),counter.get('n', 0))

