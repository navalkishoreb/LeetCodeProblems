# Write any import statements here
from math import ceil
from typing import List


def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    # Write your code here
    sorted_seats = sorted(S)
    sorted_seats.append(N + K + 1)
    count = 0
    start = 1
    for item in sorted_seats:
        end = item - K
        diff = end - start
        count += ceil(diff / (K + 1))
        start = item + K + 1
    return count
