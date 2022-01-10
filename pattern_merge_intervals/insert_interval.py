# Given a list of non-overlapping intervals sorted by their start time,
# insert a given interval at the correct position and merge all necessary
# intervals to produce a list that has only mutually exclusive intervals.
Intervals=[[1,3], [5,7], [8,12]]
NewInterval=[4,6]
Intervals2=[[1,3], [5,7], [8,12]]
NewInterval2=[4,10]
Intervals3=[[2,3],[5,7]]
NewInterval3=[1,4]

def insert_intervals(intervals, new_interv):
    intervals.append(new_interv)
    intervals.sort()
    i = 0
    while i < len(intervals) - 1:
        if intervals[i][1] >= intervals[i+1][0]:
            intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
            del intervals[i+1]
        else:
            i += 1
    return intervals

print(insert_intervals(Intervals, NewInterval))
print(insert_intervals(Intervals2, NewInterval2))
print(insert_intervals(Intervals3, NewInterval3))