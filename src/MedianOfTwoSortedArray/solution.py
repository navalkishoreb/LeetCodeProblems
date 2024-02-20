from typing import List


# expected 'm + n' to have value from 1 to 2000 only


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            # keep smallest array first
            nums1, nums2 = nums2, nums1
        a_length = len(nums1)
        b_length = len(nums2)
        total = len(nums1) + len(nums2)
        is_even = total % 2 == 0
        half_index = total // 2

        left_index, right_index = 0, len(nums1) - 1
        while True:
            mid1 = (left_index + right_index) // 2
            # half_index = (mid1 + 1) + (mid2 + 1)
            mid2 = half_index - mid1 - 2

            a_left = nums1[mid1] if 0 <= mid1 < a_length else float("-inf")
            b_left = nums2[mid2] if 0 <= mid2 < b_length else float("-inf")
            a_right = nums1[mid1 + 1] if 0 <= mid1 + 1 < a_length else float("inf")
            b_right = nums2[mid2 + 1] if 0 <= mid2 + 1 < b_length else float("inf")

            if a_left <= b_right and b_left <= a_right:
                if is_even:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
                return min(a_right, b_right)
            elif a_left > b_right:
                right_index = right_index - 1
            else:
                left_index = left_index + 1
