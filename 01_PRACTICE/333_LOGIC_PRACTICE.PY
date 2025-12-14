height = 4

# Roof
for i in range(height):
    print(" " * (height - i) + "/" + " " * (2*i) + "\\")

# Base
print(" " * (height - 1) + "_" * (2*height))

for _ in range(height):
    print(" " * (height - 1) + "|" + " " * (2*height - 2) + "|")

