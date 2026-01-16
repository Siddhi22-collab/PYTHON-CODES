s = "python is easy python is powerful"
words = s.split()
d = {}

for w in words:
    d[w] = d.get(w, 0) + 1

print(d)
