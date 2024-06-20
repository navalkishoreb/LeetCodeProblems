class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0

        def expand_from_middle(left, right) -> int:
            while left >= 0 and len(s) > right and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left - 1

        for index, _ in enumerate(s):
            len1 = expand_from_middle(index, index)
            len2 = expand_from_middle(index, index + 1)
            max_length = max(len1, len2)
            if end - start < max_length:
                start = index - ((max_length - 1) // 2)
                end = index + (max_length // 2) + 1

        return s[start:end]
