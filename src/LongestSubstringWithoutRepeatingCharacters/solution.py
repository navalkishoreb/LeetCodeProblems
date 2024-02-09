class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        max_count = 0
        left = 0
        for char in s:
            while char in substring:
                substring.remove(s[left])
                left += 1
            substring.add(char)
            max_count = max(max_count, len(substring))

        return max_count
