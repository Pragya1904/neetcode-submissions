class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        l = 0
        r = 0
        max_len = 0
        while r < len(s):
            if s[r] in chars and chars[s[r]] >= l:
                max_len = max(max_len, r - l)
               
                l = chars[s[r]] + 1
               
            chars[s[r]] = r
            r += 1
        
        return max(max_len, r - l)
        

