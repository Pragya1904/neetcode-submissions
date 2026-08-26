class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        max_num = float("inf")

        while r >= l:
            mid = (r + l) // 2
            if nums[l] <= nums[mid]:
                max_num = min(max_num, nums[l])
                l = mid + 1
            elif nums[mid] <= nums[r]:
                max_num = min(max_num, nums[mid])
                r = mid - 1
        
        return max_num