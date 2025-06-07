class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_index = 0
        right_index = len(height) - 1
        max_water_contained = 0

        while left_index < right_index :
            left_height = height[left_index]
            right_height = height[right_index]
            
            container_height = min(left_height, right_height)
            container_width = right_index - left_index
            
            water_contained = container_height * container_width
            max_water_contained = max(water_contained, max_water_contained)

            if left_height > right_height:
                right_index = right_index - 1
            else:
                left_index = left_index + 1           
        
        return max_water_contained
