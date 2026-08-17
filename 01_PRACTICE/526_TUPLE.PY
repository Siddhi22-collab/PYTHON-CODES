# TUPLE IN PYTHON

numbers = (10, 20, 30, 40, 50)

# Accessing elements
print(numbers[0])
print(numbers[-1])

# Slicing
print(numbers[1:4])
print(numbers[::-1])

# Tuple methods
print(numbers.count(20))
print(numbers.index(30))

# Built-in functions
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# Check element
print(30 in numbers)

# Tuple concatenation
a = (1, 2, 3)
b = (4, 5, 6)

print(a + b)

# Tuple repetition
print(a * 3)

# Tuple unpacking
student = ("Siddhi", 22, "Python")

name, age, subject = student

print(name)
print(age)
print(subject)