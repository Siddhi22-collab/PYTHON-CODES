
def relativeSortArray(arr1, arr2):
    count = {x: i for i, x in enumerate(arr2)}
    return sorted(arr1, key=lambda x: (count.get(x, float('inf')), x))
