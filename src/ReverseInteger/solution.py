INT_MAX = 2**31 - 1
class Solution:

    def reverse(self, a: int) -> int:
        b = 0
        toggle = 1
        if a < 0:
            toggle = -1
            a = a * toggle
        
        while a:
            r = a % 10
            b = b * 10 + r
            a = a // 10
            if b > INT_MAX:
                return 0        
        return b * toggle
