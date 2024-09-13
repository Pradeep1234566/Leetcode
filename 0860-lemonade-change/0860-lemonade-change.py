class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        count_5 = 0
        count_10 = 0
        
        for bill in bills:
            if bill == 5:
                count_5 += 1
            elif bill == 10:
                count_10 += 1
                if count_5 > 0:
                    count_5 -= 1
                else:
                    return False
            elif bill == 20:
                # Prioritize giving a 10 and a 5 as change, if possible
                if count_10 > 0 and count_5 > 0:
                    count_10 -= 1
                    count_5 -= 1
                # Otherwise, try giving three 5s as change
                elif count_5 >= 3:
                    count_5 -= 3
                else:
                    return False
        return True
