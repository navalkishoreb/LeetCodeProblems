# Write any import statements here


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    a_positions = []
    p_counter = [0]
    b_counter = [0]
    p_count = 0
    b_count = 0
    for index, item in enumerate(C):
        if item == "A":
            a_positions.append(index)

        if item == "P":
            p_count += 1

        if item == "B":
            b_count += 1

        p_counter.append(p_count)
        b_counter.append(b_count)

    total_permutations = 0
    for a_index in a_positions:
        left_start = max(0, a_index - Y)
        left_end = max(0, a_index - X + 1)

        right_start = min(N, a_index + X)
        right_end = min(N, a_index + Y + 1)

        p_left_count = p_counter[left_end] - p_counter[left_start]
        b_left_count = b_counter[left_end] - b_counter[left_start]

        p_right_count = p_counter[right_end] - p_counter[right_start]
        b_right_count = b_counter[right_end] - b_counter[right_start]

        total_permutations += (
            p_left_count * b_right_count + p_right_count * b_left_count
        )

    return total_permutations
