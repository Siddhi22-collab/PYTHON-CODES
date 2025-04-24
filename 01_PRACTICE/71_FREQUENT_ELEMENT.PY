from collections import Counter

def top_k_frequent(nums, k):
    counts = Counter(nums)
    return [item for item, _ in counts.most_common(k)]