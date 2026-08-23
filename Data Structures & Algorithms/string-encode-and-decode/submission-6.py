class Solution:
    def encode(self, strs: list[str]) -> str:
        # Store each string as: <length> + "#" + <string>
        output = []
        for s in strs:
            output.append(f"{len(s)}#{s}")
        return "".join(output)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        
        while i < len(s):
            # Find the delimiter after the length
            j = s.find("#", i)
            # Get the length of the string
            length = int(s[i:j])
            # Extract the actual string using the length
            res.append(s[j + 1 : j + 1 + length])
            # Move the pointer past the extracted string
            i = j + 1 + length
            
        return res