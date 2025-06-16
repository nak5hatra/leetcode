class Solution(object):
    def findDisappearedNumbers(self, nums):
        list_nums = []
        for i in range(1, len(nums)+1):
            list_nums.append(i)
        
        return list(set(list_nums) - set(nums)) 