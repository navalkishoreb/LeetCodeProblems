import pytest

from src.LongestSubstringWithoutRepeatingCharacters.solution import Solution


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[["uqinntq", 4], ["abcabcbb", 3]],
)
def test_lengthOfLongestSubstring(input, expected):
    actual = Solution().lengthOfLongestSubstring(s=input)
    assert actual == expected
