import sys
 
# Create an object
x = [1, 2, 3]
 
# Get reference count
ref_count = sys.getrefcount(x)
 
print("Reference count of x:", ref_count)