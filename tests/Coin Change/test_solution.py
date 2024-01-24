import pytest

from src.CoinChange.solution import Solution


@pytest.mark.parametrize(
    argnames=["coins", "amount", "expected"],
    argvalues=[[[1, 2, 3], 4, 2], [[1, 2, 5], 11, 3], [[1], 0, 0], [[2], 1, -1]],
)
def test_coinChange(coins, amount, expected):
    actual = Solution().coinChange(coins=coins, amount=amount)
    assert actual == expected
