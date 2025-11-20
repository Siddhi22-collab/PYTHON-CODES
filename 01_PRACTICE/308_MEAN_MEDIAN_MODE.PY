import statistics

# Sample data (marks scored by 30 students)
data = [56, 45, 78, 45, 60, 72, 88, 54, 49, 66,
        73, 80, 45, 56, 67, 55, 58, 62, 71, 69,
        84, 75, 48, 70, 65, 55, 77, 59, 61, 68]

# Calculate Mean
mean_value = statistics.mean(data)
print("Mean:", mean_value)

# Calculate Median
median_value = statistics.median(data)
print("Median:", median_value)

# Calculate Mode
mode_value = statistics.mode(data)
print("Mode:", mode_value)
