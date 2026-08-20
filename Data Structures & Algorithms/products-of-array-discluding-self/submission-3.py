class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        n = len(nums)
        output = [1] * n

        for i in range(n):
            output[i] = pre
            pre *= nums[i]
        
        

        for i in range(n - 1, -1, -1):
            output[i] *= post
            post *= nums[i]
        
        return output