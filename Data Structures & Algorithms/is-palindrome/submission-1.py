class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = 0
        q = len(s) - 1
        inp = s.lower()
        while p <= q:
            if inp[p].isalnum() and inp[q].isalnum():
                if inp[p] != inp[q]:
                    return False
                else:
                    p += 1
                    q -= 1
            elif not inp[p].isalnum():
                p += 1
            elif not inp[q].isalnum():
                q -= 1
        return True