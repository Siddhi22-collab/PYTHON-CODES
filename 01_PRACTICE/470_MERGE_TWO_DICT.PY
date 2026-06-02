def merge_dicts(d1, d2):
return {**d1, **d2}

data1 = {"Alice": 23, "Bob": 32}
data2 = {"Charlie": 77, "David": 19}
print(merge_dicts(data1, data2))