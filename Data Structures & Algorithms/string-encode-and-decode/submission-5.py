class Solution:

    def encode(self, strs: List[str]) -> str:
        output = "*/*".join(strs) if len(strs) > 0 else "-1"
        return output
    def decode(self, s: str) -> List[str]:
        return s.split("*/*") if s != "-1" else []