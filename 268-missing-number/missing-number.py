class Solution(object):
    def missingNumber(self, nums):

        max_value = max(nums)
        
        for i in range(max_value+1):
            if i in nums:
                continue
            else:
                return i
        return i+1