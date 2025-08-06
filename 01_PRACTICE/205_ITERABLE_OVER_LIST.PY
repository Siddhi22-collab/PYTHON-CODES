class NameList:
    def __init__(self, names):
        self.names = names

    def __iter__(self):
        return NameListIterator(self.names)

class NameListIterator:
    def __init__(self, names):
        self.names = names
        self.index = 0

    def __next__(self):
        if self.index < len(self.names):
            name = self.names[self.index]
            self.index += 1
            return name
        else:
            raise StopIteration

# Usage
names = NameList(["Alice", "Bob", "Charlie"])
for name in names:
    print(name)
