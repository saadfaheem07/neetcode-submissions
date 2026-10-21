class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        
        for i in s:
            d1[i] = 0
        
        for i in t:
            d2[i] = 0

        for i in s:
            d1[i] += 1
        
        for i in t:
            d2[i] += 1
        
        return d1 == d2