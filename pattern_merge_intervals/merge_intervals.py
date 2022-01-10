# Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
intervals = [[1,4], [2,5], [7,9]]
intervals2 = [[6,7], [2,4], [5,9]]
intervals3 = [[1,4], [2,6], [3,5]]

def merge_intervals(intervals):
    intervals.sort()
    i = 0
    new_interv = []
    while i < len(intervals)-1:
        if intervals[i][1] >= intervals[i+1][0]:
            intervals[i][1] = max(intervals[i+1][1], intervals[i][1])
            del intervals[i+1]
        else:
            i += 1
    return intervals

print(merge_intervals(intervals))
print(merge_intervals(intervals2))
print(merge_intervals(intervals3))