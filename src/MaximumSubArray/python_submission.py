class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        temp_sum = 0
        max_sum = 0
        max_element = nums[0]
        
        for data in nums:
            if data > max_element:
                max_element = data
                # print(f"setting max_element {max_element}")
            
            temp_sum += data
            if temp_sum <= 0:
                temp_sum = 0
            
            if temp_sum > max_sum:
                max_sum = temp_sum
                # print(f"setting max sum {max_sum}")
        
        # print(f"max_sum {max_sum}  max_element {max_element}")
        # print("#"*20)
        if max_sum == 0:
            return max_element
        else:
            return max_sum
            
