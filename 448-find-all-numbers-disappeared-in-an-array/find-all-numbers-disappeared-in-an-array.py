class Solution(object):
    def findDisappearedNumbers(self, nums):
        len_of_nums = len(nums)
        list_nums = []
        for i in range(1, len_of_nums+1):
            list_nums.append(i)
        
        return list(set(list_nums) - set(nums)) 