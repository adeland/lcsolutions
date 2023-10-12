class MinStack:

    def __init__(self):
        self.Minstack = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.Minstack.append(val)
        if self.stack:
            val = min(self.stack[-1], val)
        self.stack.append(val)

    def pop(self) -> None:
        self.Minstack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.Minstack[-1]
        

    def getMin(self) -> int:
        return self.stack[-1]

