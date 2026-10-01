class Solution:
    def recur_func(self, candidates: List[int], target: int, i: int):
        if self.sum == target:
            self.output.append(self.ds[:])
            return 

        if i >= len(candidates) or self.sum > target or self.sum + candidates[i] > target:
            return
       
        #take 
        self.sum += candidates[i]
        self.ds.append(candidates[i])
        self.recur_func(candidates, target, i + 1)

        #not take
        self.sum -= candidates[i]
        self.ds.pop()

        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1
            
        self.recur_func(candidates, target, i + 1)
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        self.ds = []
        self.output = []
        self.sum = 0
        candidates.sort()
        self.recur_func(candidates, target, 0)

        return self.output

        