import math
import pandas as pd
import utility


def make_dataframe(data):
    data = data[2:]  # remove directions and blank line
    labels, lefts, rights = [], [], []
    for line in data:
        label, lr = line.split('=')[0], line.split('=')[1]  # get label before '='
        label = label[:-1]  # remove pesky space
        left, right = lr.split(',')[0], lr.split(',')[1]  # get left and right
        left, right = left[2:], right[1:-1]  # remove parentheses and spaces
        labels.append(label)
        lefts.append(left)
        rights.append(right)

    return pd.DataFrame({'label': labels, 'left': lefts, 'right': rights})


def get_col_index(string):
    return 1 if string == 'L' else 2


def find_path(steps, df, num_steps, row_index, zzz=False, ghost=False):
    is_found = False
    for step in steps:
        col_index = get_col_index(step)
        next_step = df.iloc[row_index, col_index]  # read value from left/right col
        if zzz and next_step == 'ZZZ':
            is_found = True
            return num_steps, is_found, row_index
        if ghost and next_step.endswith('Z'):
            is_found = True
            return num_steps, is_found, row_index
        else:
            row_index = df.loc[df['label'] == next_step].index[0]  # find new row index
            num_steps += 1

    return num_steps, is_found, row_index


def get_steps_to_zzz(steps, df):
    row_index = df.loc[df['label'] == 'AAA'].index[0]  # start at row with 'AAA'
    num_steps = 1  # start step count at 1
    zzz_found = False

    while not zzz_found:  # continue until you find 'ZZZ'
        num_steps, zzz_found, row_index = find_path(steps, df, num_steps, row_index, zzz=True)

    return num_steps


def get_paths_as_ghost(steps, df):
    indices = df[df['label'].str.endswith('A')].index.tolist()  # indices of values ending in 'A'
    endpoints = []

    for i in indices:
        row_index = i
        num_steps = 1
        z = False
        while not z:  # continue until you find value that ends in 'Z'
            num_steps, z, row_index = find_path(steps, df, num_steps, row_index, ghost=True)
        endpoints.append(int(num_steps))

    return math.lcm(*endpoints)  # full disclosure - looked up a hint to use LCM after trying brute force!


def solve_d8(data_path):
    data = utility.read_file(data_path)
    steps = list(data[0])
    df = make_dataframe(data)
    q1_answer = get_steps_to_zzz(steps, df)
    q2_answer = get_paths_as_ghost(steps, df)
    print('The number of steps from AAA to ZZZ is', q1_answer)
    print('The number of steps from all As to all Zs as a ghost is', q2_answer)


if __name__ == '__main__':
    path = "C:\\Users\\bmvan\PycharmProjects\\aoc_2023\data\d8.txt"
    solve_d8(path)