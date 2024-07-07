import pytest

from src.DirectorOfPhotography.solution import getArtisticPhotographCount


@pytest.mark.parametrize(
    argnames=["N", "C", "X", "Y", "expected_result"],
    argvalues=[
        [
            5,
            "APABA",
            1,
            2,
            1,
        ],
        [
            5,
            "APABA",
            1,
            2,
            1,
        ],
        [
            8,
            ".PBAAP.B",
            1,
            3,
            3,
        ],
    ],
)
@pytest.mark.timeout(1)
@pytest.mark.limit_memory("100 KB")
def test_solution(N, C, X, Y, expected_result):
    actual_result = getArtisticPhotographCount(N=N, C=C, X=X, Y=Y)
    assert actual_result == expected_result
