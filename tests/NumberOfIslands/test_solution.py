import pytest

from src.NumberOfIslands.solution import Solution


@pytest.mark.parametrize(
    argnames=["input_data", "expected_result"],
    argvalues=[
        [
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ],
        [
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
        ],
        [[["1", "0", "1", "1", "0", "1", "1"]], 3],
        [[["0"]], 0],
    ],
)
@pytest.mark.timeout(1)
@pytest.mark.limit_memory("100 KB")
def test_solution(input_data, expected_result):
    actual_result = Solution().numIslands(grid=input_data)
    assert actual_result == expected_result
