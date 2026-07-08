class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countMap ={}
        for i in range(len(s)):
            countMap[s[i]] = 1 + countMap.get(s[i], 0)
            countMap[t[i]] = countMap.get(t[i], 0) - 1
        return all(v == 0 for v in countMap.values())
        
