class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vis = {}
        for i in range(len(nums)):
            if  target - nums[i] in vis:
                return [vis[target - nums[i]],i]
            vis[nums[i]] = i