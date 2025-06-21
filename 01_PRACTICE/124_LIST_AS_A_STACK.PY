stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack after pushes:", stack)

# Pop element
print("Popped:", stack.pop())

# Peek (top element)
print("Top element:", stack[-1])

# Is stack empty?
print("Is empty?", len(stack) == 0)
