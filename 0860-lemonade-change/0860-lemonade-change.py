class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        count_5 = 0
        count_10 = 0
        count_20 = 0
        for i in bills:
            if i == 5:
                count_5 += 1
            elif i == 10:
                count_10 += 1
                if count_5 < 1:
                    return False
            elif i == 20:
                if count_5 < 3 or (count_10<1 and count_5<1):
                    return False
        return True
        