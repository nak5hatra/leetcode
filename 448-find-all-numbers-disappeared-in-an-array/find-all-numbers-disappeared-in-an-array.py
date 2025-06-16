class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        list_nums = []
        num_set = set(nums)
        for i in range(1, len(nums)+1):
            if i not in num_set:
                list_nums.append(i)
        return list_nums