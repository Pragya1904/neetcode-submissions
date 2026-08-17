class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p = 0 
        q = len(numbers) - 1
        
        while p < q:
            agg = numbers[p] + numbers[q]
            if agg == target:
                return [p + 1, q + 1]
            elif agg < target:
                p += 1
            else:
                q -= 1