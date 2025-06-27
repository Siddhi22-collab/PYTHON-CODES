class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage
s = Stack()
s.push(5)
s.push(10)
print("Top:", s.peek())
print("Size:", s.size())
print("Popped:", s.pop())
print("Is empty?", s.is_empty())
