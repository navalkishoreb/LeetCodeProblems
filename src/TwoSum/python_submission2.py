class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = dict()
        
        for index in range(len(nums)):
            num_dict[nums[index]]=index
            
        for index in range(len(nums)):
            mirror_value = target - nums[index]
            # print(f"mirror value {mirror_value}")
            if mirror_value in num_dict:
                mirror_index = num_dict[mirror_value]
                if mirror_index != index:
                    # print(f"mirror index {mirror_index}")
                    return [index, mirror_index]
