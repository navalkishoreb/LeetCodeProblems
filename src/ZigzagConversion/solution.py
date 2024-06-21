class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = [[] for _ in range(numRows)]
        direction = 1
        index = 0
        for char in s:
            matrix[index].append(char)
            index += direction
            if index >= numRows or index < 0:
                # Change direction
                direction *= -1
                index += 2 * direction

        all_chars = [cell for row in matrix for cell in row]
        return "".join(all_chars)
