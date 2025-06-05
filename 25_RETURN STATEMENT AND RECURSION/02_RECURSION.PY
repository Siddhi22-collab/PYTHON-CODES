def hello():
    print("Hello, World!")
    return hello()
print(hello())  # Output: Hello, World! followed by a recursive call