class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    # Insert at the beginning
    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Delete a node by value
    def delete(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                if curr.prev:
                    curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                if curr == self.head:
                    self.head = curr.next
                return
            curr = curr.next

    # Traverse forward
    def display_forward(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.data)
            curr = curr.next
        return elements

    # Traverse backward
    def display_backward(self):
        elements = []
        curr = self.head
        if not curr:
            return elements
        while curr.next:
            curr = curr.next
        while curr:
            elements.append(curr.data)
            curr = curr.prev
        return elements

    # Search for a node
    def search(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False


# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.pre
