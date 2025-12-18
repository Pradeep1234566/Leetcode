class Solution(object):
    def myAtoi(self, s):
        left = 0
        n = len(s)
        result = []
        sign = 1
        count_signs = 0

        while left < n:
            if count_signs > 1:
                break

            if s[left] == " " and not result and count_signs == 0:
                left += 1

            elif ((s[left] == "-" or s[left] == "+") and not result):
                count_signs += 1
                if count_signs > 1:
                    return 0
                if s[left] == "-":
                    sign = -1
                left += 1

            elif s[left].isdigit():
                result.append(s[left])
                left += 1

            else:
                break

        if not result:
            return 0

        num = sign * int("".join(result))

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num
