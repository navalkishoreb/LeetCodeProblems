class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = set(nums)
        
        for index,value in enumerate(nums):
            mirror_value = target - value
            print(f"mirror value {mirror_value}")
            if mirror_value in num_set:
                mirror_index = nums.index(mirror_value)
                if mirror_index != index:
                    print(f"mirror index {mirror_index}")
                    return [index, mirror_index]
