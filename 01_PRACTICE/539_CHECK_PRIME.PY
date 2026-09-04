def is_prime(num):
if num <= 1:
return False
for i in range(2, int(num**0.5) + 1):
if num % i == 0:
return False
return True

print(is_prime(11)) # True



Merge Two Dictionaries


List Comprehension for Squares


File Reading


Sorting by Value in a Dictionary

Key Takeaways:

Use list comprehensions for concise loops.

Prefer with statements for file handling.

Apply dictionary unpacking for merging.

Optimize algorithms (e.g., prime check up to √n).

These examples cover loops, conditionals, functions, recursion, comprehensions, and file I/O, which are essential for interviews and daily coding tasks.



3 sources
