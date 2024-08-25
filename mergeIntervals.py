intervals = [[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]]


def merge(intervals):

    intervals.sort(key = lambda x : x[0])
    results = [intervals[0]]
    pointer = 0

    for i in range(1, len(intervals)):

        if results[pointer][1] >= intervals[i][0]:
            results[pointer] = [
                results[pointer][0],
                max(results[pointer][1], intervals[i][1]),
            ]

        else:
            results.append(intervals[i])
            pointer += 1

    return results

print(merge(intervals))