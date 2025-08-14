import time
import random

# Time Complexity Reference Table
time_complexities = {
    "List": {
        "Access (lst[i])": "O(1)",
        "Append (lst.append)": "O(1) amortized",
        "Insert at index": "O(n)",
        "Search in list": "O(n)",
        "Sort (sorted(lst))": "O(n log n)"
    },
    "Dictionary": {
        "Access by key": "O(1) average",
        "Insert / Update": "O(1) average",
        "Delete by key": "O(1) average"
    },
    "Set": {
        "Add": "O(1) average",
        "Remove": "O(1) average",
        "Membership test": "O(1) average"
    }
}

# Display table
print("\n=== Time Complexity Cheat Sheet ===\n")
for ds, ops in time_complexities.items():
    print(f"{ds}:")
    for op, tc in ops.items():
        print(f"  {op:<25} -> {tc}")
    print()

# Example: Measure actual execution time
def measure_time(func, *args):
    start = time.time()
    func(*args)
    return time.time() - start

# Test functions
def linear_search(lst, target):
    for item in lst:
        if item == target:
            return True
    return False

def binary_search(sorted_lst, target):
    low, high = 0, len(sorted_lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_lst[mid] == target:
            return True
        elif sorted_lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Test dataset
n = 1_000_000
lst = list(range(n))
target = random.randint(0, n-1)

print("=== Measuring Execution Times ===")
print("Linear Search:", measure_time(linear_search, lst, target), "seconds")
print("Binary Search:", measure_time(binary_search, lst, target), "seconds")
print("Built-in 'in':", measure_time(lambda arr, x: x in arr, lst, target), "seconds")
