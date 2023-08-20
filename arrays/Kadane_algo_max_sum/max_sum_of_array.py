class Solution(object):
    def maxSubArray(self, nums):
        curr = 0
        fin = -float('inf')

        for i in range(0,len(nums)):
            curr = max(nums[i] , curr+nums[i])
            fin  = max(curr , fin)
        return fin