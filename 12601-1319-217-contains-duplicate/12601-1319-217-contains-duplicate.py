class Solution(object):
    def containsDuplicate(self, nums):
        temp_len = len(nums)
        my_set_len = len(set(nums))
        if temp_len == my_set_len:
            return False
        else:
            return True
        