class Solution:
    def build_counter(self, string: str):
        arr = [0] * 26
        for char in string:
            idx = ord(char) - ord('a')
            arr[idx] += 1
        return arr

    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        s1_counter = self.build_counter(s1)
        s2_counter = self.build_counter(s2[:k])

        for r in range(k, len(s2)):
            if s1_counter == s2_counter:
                return True
        
            exclude_char_idx = ord(s2[r - k]) - ord('a')
            s2_counter[exclude_char_idx] -= 1

            inc_char_idx = ord(s2[r]) - ord('a')
            s2_counter[inc_char_idx] += 1

        return s1_counter == s2_counter