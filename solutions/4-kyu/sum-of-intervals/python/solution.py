def sum_of_intervals(intervals):
    return len(set.union(*(set(range(*x)) for x in intervals)))