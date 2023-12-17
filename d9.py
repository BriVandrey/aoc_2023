import numpy as np
import re
import utility


def get_last_value(arrays, idx, subtract=False):
    val_to_return, val = 0, 0  # start with 0's
    for i, array in enumerate(arrays[:-1]):  # iterate up to the second to last array
        next_val = arrays[i + 1][idx]
        if subtract:
            val = next_val - val
        else:
            val = next_val + val
        val_to_return = val

    return val_to_return


def get_history(numbers, diffs):
    if np.all(diffs == 0):
        return 0
    else:  # get list of difference arrays
        arrays = []
        arrays.append(numbers)
        arrays.append(diffs)

        while not np.all(diffs == 0):  # check if array is all 0's
            diffs = np.diff(diffs)  # get array of differences
            arrays.append(diffs)

        arrays.reverse()  # reverse so last array (all 0's) is first because who likes going backwards
        last_value = get_last_value(arrays, -1)
        last_value_front = get_last_value(arrays, 0, subtract=True)

        return last_value, last_value_front


def extrapolate_values(data):
    vals, vals_front = [], []
    for line in data:
        numbers = [int(n) for n in re.findall(r'-?\d+', line)]
        val, val2 = get_history(numbers, np.diff(numbers))
        vals.append(val)
        vals_front.append(val2)

    return sum(vals), sum(vals_front)


def solve_d9(data_path):
    data = utility.read_file(data_path)
    q1_answer, q2_answer = extrapolate_values(data)
    print('The sum of extrapolated values forwards is', q1_answer)
    print('The sum of extrapolated values backwards is', q2_answer)


if __name__ == '__main__':
    path = "C:\\Users\\bmvan\PycharmProjects\\aoc_2023\data\d9.txt"
    solve_d9(path)