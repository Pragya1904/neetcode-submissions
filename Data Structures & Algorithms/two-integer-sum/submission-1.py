class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #approach 1:
        # nested loops --> time O(n^2) and space is O(1)

        # approach 2:
        # sort the input and maintain the original index with it and use simple 2 pointers then ---> time O(nlogn) for sorting and space O(n) for storing map

        #approach 3:
        # maintain a hash map like if target = p + q then map would look like {p: p's index} so if we are at index of q then check if target - q is a key in the map or not 
        # space is O(n) and time is O(n) in avg, worst case finding key in map is O(n) in case of collision but it's rare and avg case is O(1)

        # below is the implementation using approach 3
        pairs = {}

        for i in range(len(nums)):
            required = target - nums[i]
            if required in pairs:
                return [pairs[required], i]
            elif nums[i] not in pairs:
                pairs[nums[i]] = i

        return []
            
