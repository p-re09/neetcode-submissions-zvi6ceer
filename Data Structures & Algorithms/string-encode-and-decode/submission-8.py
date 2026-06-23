class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''.join(str(len(s)) + '#' + s for s in strs)
        return encoded

    def decode(self, encoded_string: str) -> List[str]:
        result = []
        i = 0
        while i < len(encoded_string):
            j = i

            while encoded_string[j] != '#':
                j += 1

            length = int(encoded_string[i:j])            
            word = encoded_string[j + 1 : j + 1 + length]

            result.append(word)

            i = j + 1 + length

        return result



