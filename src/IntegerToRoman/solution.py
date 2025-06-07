class Solution:
    def intToRoman(self, num: int) -> str:
        
        symbols =     ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V" , "IV", "I"]
        roman_scale = [1000, 900, 500, 400,  100,  90,  50,  40,    10,   9,  5  ,   4,   1]
        roman_index = 0
        roman = []
        while num:
            # print(f"{num=!r} {roman_index=!r} {roman_scale[roman_index]=!r}")
            if num >= roman_scale[roman_index]:
                num = num - roman_scale[roman_index]
                sym = symbols[roman_index]
                roman.append(sym)
            else:
                roman_index = roman_index + 1
        return "".join(roman)

