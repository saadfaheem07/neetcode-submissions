class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        st = ''
        for i in s:
            if i.isalnum():
                st += i

        start = 0
        end = len(st) - 1
        
        while start <= end:
            if st[start] != st[end]:
                return False
            
            start += 1
            end -= 1
        
        return True