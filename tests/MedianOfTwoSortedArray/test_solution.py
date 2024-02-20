import pytest

from src.MedianOfTwoSortedArray.solution import Solution


@pytest.mark.parametrize(
    argnames=["nums1", "nums2", "expected"],
    argvalues=[
        [[1, 3], [2], 2],
        [[1], [2], 1.5],
        [[1], [], 1],
        # [[], [], 0],
        [[1, 2], [3, 4], 2.5],
        [[1, 3, 4, 7, 10, 12], [2, 3, 6, 15], 5],
    ],
)
@pytest.mark.timeout(1)
def test_findMedianSortedArrays(nums1, nums2, expected):
    actual = Solution().findMedianSortedArrays(nums1=nums1, nums2=nums2)
    assert actual == expected
