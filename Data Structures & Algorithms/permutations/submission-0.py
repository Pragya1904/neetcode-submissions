class Solution:
    def recur(self, nums: List[int]):
        if len(self.ds) == len(nums):
            self.output.append(self.ds[:])
            return
        
        for i in range(len(nums)):
            if i not in self.freq:
                self.freq[i] = 1
                self.ds.append(nums[i])

                self.recur(nums)

                self.freq.pop(i)
                self.ds.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        self.ds = []
        self.freq = {}

        self.recur(nums)

        return self.output
        