class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = dict()
        
            
        for index in range(len(nums)):
            pair = target - nums[index]
            
            if nums[index] in num_dict:
                return [index,num_dict[nums[index]]]
            
            num_dict[pair] = index
            
        return []
