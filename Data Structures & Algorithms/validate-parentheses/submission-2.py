class Solution:
    def isPair(self,a: char,b: char) -> bool:
        return (a == '(' and b == ')') or (a == '[' and b == ']') or (a == '{' and b == '}')

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if stack:
                if self.isPair(stack[-1],c):
                    stack.pop()
                    continue
                
            stack.append(c)
        
        return True if not stack else False