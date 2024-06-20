class Solution:
    def is_pallindrome(self, s: str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        dp = {}

        def longest_palindrome(s: str) -> str:
            if not s:
                return ""
            if s in dp:
                return dp[s]
            if self.is_pallindrome(s):
                dp[s] = s
                return s

            right_substring = longest_palindrome(s[1:])
            left_substring = longest_palindrome(s[:-1])
            if len(right_substring) > len(left_substring):
                result = right_substring
            else:
                result = left_substring

            dp[s] = result
            return result

        return longest_palindrome(s=s)
