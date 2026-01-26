# Word count
s = "hello world hello"
words = s.split()
d = {}

for w in words:
    d[w] = d.get(w, 0) + 1

print(d)
