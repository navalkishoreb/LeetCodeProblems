class Solution:
    def isPalindrome(self, n: int) -> bool:
        if n < 0:
            return False
        def reverse(x):
            b = 0
            while x:
                r = x % 10
                b = b * 10 + r
                x = x // 10
            return b
        return reverse(n) == n       
