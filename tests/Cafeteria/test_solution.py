import pytest

from src.Cafeteria.solution import getMaxAdditionalDinersCount


@pytest.mark.parametrize(
    argnames=["N", "K", "M", "S", "expected_result"],
    argvalues=[
        [
            10,
            1,
            2,
            [2, 6],
            3,
        ],
        [
            15,
            2,
            3,
            [11, 6, 14],
            1,
        ],
    ],
)
@pytest.mark.timeout(1)
@pytest.mark.limit_memory("100 KB")
def test_solution(N, K, M, S, expected_result):
    actual_result = getMaxAdditionalDinersCount(N=N, K=K, M=M, S=S)
    assert actual_result == expected_result
