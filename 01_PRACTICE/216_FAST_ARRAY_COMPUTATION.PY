import numpy as np

# Generate large dataset (simulate)
data = np.random.rand(10_000_000)

# Basic analysis
print("Mean:", np.mean(data))
print("Std Dev:", np.std(data))
print("Max:", np.max(data))
print("Min:", np.min(data))
