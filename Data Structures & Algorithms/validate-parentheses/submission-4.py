class Solution:
    def isPair(self, s: str, t: str) -> bool:
        return (s == '(' and t == ')') or (s == '[' and t == ']') or (s == '{' and t == '}')

    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if stack:
                if self.isPair(stack[-1], i):
                    stack.pop()
                    continue

            stack.append(i)
        
        return True if not stack else False