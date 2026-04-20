def merge_intervals(intervals):
    intervals.sort()
    merged = [intervals[0]]

    for i in intervals[1:]:
        if i[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], i[1])
        else:
            merged.append(i)

    return merged