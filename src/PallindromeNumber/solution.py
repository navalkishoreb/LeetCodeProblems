class Solution:
    def isPalindrome(self, x: int) -> bool:
        input_string = str(x)
        reverse_string = input_string[::-1]
        return input_string == reverse_string
        
