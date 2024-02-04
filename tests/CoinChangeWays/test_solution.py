import pytest

from src.CoinChangeWays.solution import Solution


@pytest.mark.parametrize(
    argnames=["coins", "amount", "expected_ways"],
    # argvalues=[[[1, 2, 5], 5, 4]],
    # argvalues=[[[1, 2, 5], 8, 7]],
    # argvalues=[[[7], 0, 1]],
    # argvalues=[[[1, 2, 5], 500, 12701]],
    argvalues=[[[11, 24, 37, 50, 63, 76, 89, 102], 5000, 992951208]],
    # argvalues=[[[1, 2, 5], 5, 4], [[2], 3, 0], [[10], 10, 1]],
)
@pytest.mark.timeout(1)
def test_coinChange(coins, amount, expected_ways):
    actual = Solution().change(coins=coins, amount=amount)
    assert actual == expected_ways
