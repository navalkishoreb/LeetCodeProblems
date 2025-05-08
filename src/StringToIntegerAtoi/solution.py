INT_MAX = 2**31 - 1
INT_MIN = -2**31
class Solution:
    def myAtoi(self, s: str) -> int:
        # ignore any leading whitespace
        s = s.lstrip()
        if not s:
            return 0
        
        # check symbol
        symbol = s[0]
        sign = 1
        if symbol == "-":
            sign = -1
            s = s[1:]
        elif symbol == "+":
            s = s[1:]
        
        number = []
        for char in s:
            # print(char)
            if not char.isdigit():
                # break when first non digit encountered
                break
            number.append(char)

        if not number:
            return 0

        actual_number = int("".join(number)) * sign
        if actual_number < INT_MIN:
            return INT_MIN
        if actual_number > INT_MAX:
            return INT_MAX
        return actual_number

