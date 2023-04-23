class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return None
        x = self.stack.pop()
        if x == self.max_stack[-1]:
            self.max_stack.pop()
        return x

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def peekMax(self) -> int:
        if not self.max_stack:
            return None
        return self.max_stack[-1]

    def popMax(self) -> int:
        if not self.max_stack:
            return None
        max_val = self.max_stack.pop()
        new_stack = []
        while self.stack[-1] != max_val:
            new_stack.append(self.stack.pop())
        self.stack.pop()
        while new_stack:
            self.push(new_stack.pop())
        return max_val
