class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringMap = {}
        for str in strs:
            freq = [0] * 26
            for char in str:
                charIndex = ord(char) - ord('a')
                freq[charIndex] += 1
            if tuple(freq) in stringMap:
                stringMap[tuple(freq)].append(str)
            else:
                stringMap[tuple(freq)] = [str]
        return list(stringMap.values())                
