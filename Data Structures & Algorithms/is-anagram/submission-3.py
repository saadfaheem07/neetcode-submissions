class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = {key:0 for key in s}, {key:0 for key in t}
        
        for i in s:
            d1[i] += 1
        for i in t:
            d2[i] += 1
        
        if d1 == d2:
            return True
        return False