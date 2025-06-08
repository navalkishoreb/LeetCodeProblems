class Solution:
    def romanToInt(self, s: str) -> int:
        symbols =     ["M", "D", "C", "L",  "X",  "V" , "I"]
        roman_scale = [1000, 500,100, 50, 10, 5, 1]
        symbol_table = dict(zip(symbols, roman_scale))
        roman_index = 0

        reversed_string = s[::-1]
        direction = 1
        total = 0
        previous_value= roman_scale[-1]
        for char in reversed_string:
            value = symbol_table[char]
            if value < previous_value:
                direction = -1
            else:
                direction = 1
            previous_value = value
            value = value * direction
            # print(value)
            total = total + value
        return total
