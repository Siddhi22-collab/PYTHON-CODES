def selection_sort(a):
    for i in range(len(a)):
        min_i = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_i]:
                min_i = j
        a[i], a[min_i] = a[min_i], a[i]

a = [64, 25, 12, 22, 11]
selection_sort(a)
print(a)
