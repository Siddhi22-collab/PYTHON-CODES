class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if self.stack:
            value = self.stack.pop()
            if value == self.min_stack[-1]:
                self.min_stack.pop()
            return value
        return None

    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None

# Usage
s = MinStack()
s.push(3)
s.push(5)
s.push(2)
print(s.get_min())  # Output: 2
s.pop()
print(s.get_min())  # Output: 3
