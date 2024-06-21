import pytest

from src.ZigzagConversion.solution import Solution


@pytest.mark.parametrize(
    argnames=["input_string", "num_rows", "expected_string"],
    argvalues=[
        ["PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"],
        ["PAYPALISHIRING", 4, "PINALSIGYAHRPI"],
        ["A", 1, "A"],
    ],
)
@pytest.mark.timeout(1)
@pytest.mark.limit_memory("100 KB")
def test_zig_zag_conversion(input_string, num_rows, expected_string):
    actual_string = Solution().convert(s=input_string, numRows=num_rows)
    assert actual_string == expected_string
