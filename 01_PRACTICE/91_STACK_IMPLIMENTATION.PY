class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None  # Represents the top of the stack

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Link new node to current head
        self.head = new_node       # Update head to new node

    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        popped_node = self.head
        self.head = self.head.next  # Move head to next node
        return popped_node.data

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.head.data
