import pytest

from src.DeleteAndEarn.solution import Solution
from src.DeleteAndEarn.solution_with_sliding_window import (
    Solution as SlidingwindowSolution,
)


@pytest.mark.parametrize(
    argnames=["input_list", "expected_result"],
    argvalues=[[[3, 4, 2], 6], [[2, 2, 3, 3, 3, 4], 9]],
)
@pytest.mark.timeout(1)
@pytest.mark.limit_memory("100 KB")
def test_delete_and_earn_recursive(input_list, expected_result):
    actual_result = Solution().deleteAndEarn(nums=input_list)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    argnames=["input_list", "expected_result"],
    argvalues=[[[3, 4, 2], 6], [[2, 2, 3, 3, 3, 4], 9]],
)
@pytest.mark.timeout(1)
@pytest.mark.limit_memory("100 KB")
def test_delete_and_earn_for_loop(input_list, expected_result):
    actual_result = SlidingwindowSolution().deleteAndEarn(nums=input_list)
    assert actual_result == expected_result
