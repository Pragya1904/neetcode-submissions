class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        temp = set(nums)
        # print(temp)
        difference = len(nums) - len(temp)
        return bool(difference)