class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = []
        max_count = 0
        for char in list(s):
            if char in substring:
                for i in range(substring.index(char) + 1):
                    substring.pop(0)
                substring.append(char)
                max_count = max(len(substring), max_count)
            else:
                substring.append(char)
                max_count = max(len(substring), max_count)
        return max_count
