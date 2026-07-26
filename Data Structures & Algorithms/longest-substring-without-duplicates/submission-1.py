class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueSet = set()
        l = 0
        maxLen = 0

        for r in range(len(s)):
            while s[r] in uniqueSet:
                uniqueSet.remove(s[l])
                l += 1
            
            uniqueSet.add(s[r])
            maxLen = max(maxLen,r - l + 1)
        
        return maxLen