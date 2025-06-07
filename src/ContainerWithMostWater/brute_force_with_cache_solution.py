class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        cache = {}
        for current_index, current_value in enumerate(height):
            for other_index, other_value in enumerate(height[current_index + 1:], start=current_index+1):
                if (current_index, other_index) in cache:
                    area = cache[(current_index, other_index)]
                else:
                    min_height = min(current_value, other_value)
                    width = other_index - current_index
                    area = min_height * width
                    cache[(current_index, other_index)] = area
                # print(f"{current_index}, {current_value}, {other_index}, {other_value}, {min_height}, {width}, {area}")
                if area > max_area:
                    max_area = area
        return max_area       
