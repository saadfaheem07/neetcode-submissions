class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float('inf')

    def push(self, val: int) -> None:
        self.minVal = min(val, self.minVal)
        self.stack.append([val, self.minVal])

    def pop(self) -> None:
        self.stack.pop()

        if self.stack:
            self.minVal = self.stack[-1][1]
        else:
            self.minVal = float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
