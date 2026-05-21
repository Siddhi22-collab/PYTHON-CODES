# Simple Linked List in Python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create Nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Connect Nodes
node1.next = node2
node2.next = node3

# Print Linked List
temp = node1

while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("NULL")