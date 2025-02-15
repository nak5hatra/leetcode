class Solution(object):
    def findDisappearedNumbers(self, nums):
        length_nums = len(nums)
        myset = set(nums)
        return_lst = []
        for i in range(1, length_nums+1):
            if i in myset:
                continue
            else:
                return_lst.append(i)
        return return_lst