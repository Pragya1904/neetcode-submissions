class Solution:
    def generate_key(self, word: str) -> str:
        word = sorted(word)
        return "".join(word)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}
        for input_word in strs:
            word = self.generate_key(input_word)
            if word not in temp:
                temp[word] = [input_word]
            else:
                temp[word].append(input_word)

        output = []

        for key, value in temp.items():
            output.append(value)

        return output