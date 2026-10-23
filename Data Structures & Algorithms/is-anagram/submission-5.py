class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        
        for i in t:
            d[i] -= 1

        if all(v == 0 for v in d.values()):
            return True
        return False