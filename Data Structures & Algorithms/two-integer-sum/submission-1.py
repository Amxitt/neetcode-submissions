class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i in range(len(nums)):
            if(target - nums[i] not in values):
                values[nums[i]] = i
            
            else:
                return [values[target-nums[i]], i]
