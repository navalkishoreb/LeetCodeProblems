class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        max_area = 0
        area = 0

        while(l<r):
            width = r - l
            if height[l] < height[r]:
                area = width * height[l]
                l +=1
            else:
                area = width * height[r]
                r -=1
            max_area = max(max_area, area)        
        return max_area
