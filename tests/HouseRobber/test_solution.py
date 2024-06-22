import pytest

from src.HouseRobber.solution import Solution


# from src.HouseRobber.python_submission_linear_stucture import Solution


@pytest.mark.parametrize(
    argnames=["input_list", "expected_result"],
    argvalues=[
        [[1, 2, 3, 1], 4],
        [[2, 7, 9, 3, 1], 12],
        [[1, 2], 2],
        [
            [
                104,
                209,
                137,
                52,
                158,
                67,
                213,
                86,
                141,
                110,
                151,
                127,
                238,
                147,
                169,
                138,
                240,
                185,
                246,
                225,
                147,
                203,
                83,
                83,
                131,
                227,
                54,
                78,
                165,
                180,
                214,
                151,
                111,
                161,
                233,
                147,
                124,
                143,
            ],
            3176,
        ],
    ],
)
@pytest.mark.timeout(1)
@pytest.mark.limit_memory("100 KB")
def test_house_robber(input_list, expected_result):
    actual_result = Solution().rob(nums=input_list)
    assert actual_result == expected_result
