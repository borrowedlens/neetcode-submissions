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
        while i < (len(s)):
            j = i
            while s[i] != "#":
                i += 1
            length = int(s[j:i])
            j = i + 1
            decoded_string = s[j: j + length]
            decoded.append(decoded_string)
            i = j + length
        return decoded
            