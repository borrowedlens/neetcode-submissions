class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append("#")
            encoded.append(s)
        return "".join(encoded)
            

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[i] != "#":
                i += 1
            length = int(s[j:i])
            decoded_string = s[i + 1: i + 1 + length]
            decoded.append(decoded_string)
            i = i + length + 1
        return decoded
            