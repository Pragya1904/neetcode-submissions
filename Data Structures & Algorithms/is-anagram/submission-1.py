class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        
        if len(s) != len(t):
            return False 
        for ch in s:
            if ch not in chars:
                chars[ch] = 1
            else:
                chars[ch] += 1
            
        for ch in t:
            if ch in chars:
                chars[ch] -= 1
                if chars[ch] == 0:
                    chars.pop(ch)
    
        
        return False if chars else True