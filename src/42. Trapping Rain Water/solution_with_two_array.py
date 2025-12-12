class Solution:
    def trap(self, height: List[int]) -> int:
    
        leftMax = 0
        left = []
        for h in height:
            leftMax = max(h, leftMax)
            left.append(leftMax)
        
        rightMax = 0
        right = []
        for h in height[::-1]:
            rightMax = max(h, rightMax)
            right.append(rightMax)
        
        right = right[::-1]

        # print(left)
        # print(right)
        res = []
        for leftMax, rightMax, h in zip(left, right, height):
            value = min(leftMax, rightMax) - h
            if value > 0:
                res.append(value)
            else:
                res.append(0)
        
        # print(res)
        return sum(res)
