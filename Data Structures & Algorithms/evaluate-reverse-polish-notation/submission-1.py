class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []

        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            
            else:
                op2 = stack.pop()
                op1 = stack.pop()

                if i == '+':
                    stack.append(op1 + op2)
                elif i == '-':
                    stack.append(op1 - op2)
                elif i == '*':
                    stack.append(op1 * op2)
                else:
                    stack.append(int(op1 / op2))
        
        return stack[-1]