class Solution(object):
    def missingNumber(self, nums):
        range_len = sum(range(len(nums)+1))
        return range_len - sum(nums)