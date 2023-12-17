import numpy as np
import re
import utility


def get_last_value(arrays):
    val_to_return, val = 0, 0  # start with 0's
    for i in range(0, len(arrays) - 1):
        next_val = arrays[i + 1][-1]
        val = next_val + val
        if i == len(arrays) - 2:  # stop when reaching the second to last value
            val_to_return = val
    return val_to_return


def get_history(diffs):
    if np.all(diffs == 0):
        return 0
    else:  # get list of difference arrays
        arrays = []
        arrays.append(diffs)

        while not np.all(diffs == 0):  # check if array is all 0's
            diffs = np.diff(diffs)  # get array of differences
            arrays.append(diffs)

        arrays.reverse()  # reverse so last array (all 0's) is first because who likes going backwards
        last_value = get_last_value(arrays)

        return last_value


def extrapolate_values(data):
    vals = []
    for line in data:
        numbers = [int(n) for n in re.findall(r'-?\d+', line)]
        val = get_history(np.diff(numbers))
        vals.append(val)

    return sum(vals)


def solve_d9(data_path):
    data = utility.read_file(data_path)
    q1_answer = extrapolate_values(data)
    print(q1_answer)


if __name__ == '__main__':
    path = "C:\\Users\\bmvan\PycharmProjects\\aoc_2023\data\d9.txt"
    solve_d9(path)