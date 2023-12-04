"""
Q1:
The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If
you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers
and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part
number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine
schematic?

Q2:
The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is
adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which
gear needs to be replaced.

What is the sum of all of the gear ratios in your engine schematic?

"""
import numpy as np
import utility


def pad_array(array):
    padded_array = np.full((array.shape[0] + 2, array.shape[1] + 2), '.', dtype=array.dtype)  # pad with '.'
    padded_array[1:-1, 1:-1] = array
    return padded_array


def check_array_for_symbols(array):
    array_string = array.astype(str)
    symbols = ~np.core.defchararray.isalnum(array_string) & (array_string != '.')  # not a letter, number, or '.'
    return np.any(symbols)  # True if symbol found


def subset_array_around_number(array, row_index, number_indices):
    number_to_return = 0

    if len(number_indices) > 0:  # won't need to process first or last row ('.' only)
        x_min, x_max = row_index - 1, row_index + 2  # rows to subset
        y_min, y_max = number_indices[0] - 1, number_indices[-1] + 2  # cols to subset
        subset = array[x_min:x_max, y_min:y_max]
        symbol_exists = check_array_for_symbols(subset)

        if symbol_exists:
            number_slice = array[row_index, y_min+1:y_max-1]
            number_to_return = int(''.join(str(num) for num in number_slice))

    return number_to_return


def get_sum_of_part_numbers(array):
    cumulative_sum = 0  # start sum at 0
    array = pad_array(array)  # pad with '.' so I don't need to handle edge cases

    for i in range(len(array)):
        row = array[i]  # get row from index
        number_indices = [i for i, char in enumerate(row) if any(c.isdigit() for c in char)]  # indices of numbers
        grouped_indices = np.split(number_indices, np.where(np.diff(number_indices) != 1)[0] + 1)  # indices grouped by number

        for group in grouped_indices:
            part_number = subset_array_around_number(array, i, group)  # subset array and return number if symbol

            if part_number > 0:
                cumulative_sum += part_number  # add part number to cumulative sum

    return cumulative_sum


def find_adjacent_numbers(array):
    numbers = []
    indices_around_gear = [3, 4, 5]

    for i in range(len(array)):
        row = array[i]  # get row from index
        number_indices = [i for i, char in enumerate(row) if any(c.isdigit() for c in char)]  # indices of numbers
        grouped_indices = np.split(number_indices, np.where(np.diff(number_indices) != 1)[0] + 1)  # indices grouped by number

        for group in grouped_indices:
            if np.any(np.isin(group, indices_around_gear)):  # check if contains adjacent to gear
                number = int(''.join(str(num) for num in row[group]))
                numbers.append(number)

    return numbers


def find_numbers_around_gear(array, row_index, gear_index):
    x_min, x_max = row_index - 1, row_index + 2  # rows to subset
    y_min, y_max = gear_index - 4, gear_index + 5  # cols to subset
    subset = array[x_min:x_max, y_min:y_max]
    adjacent_numbers = find_adjacent_numbers(subset)

    return adjacent_numbers


def find_gears(array):
    cumulative_sum = 0  # start sum at 0
    array = pad_array(array)  # pad with '.' so I don't need to handle edge cases
    gear = '*'

    for i in range(len(array)):
        row = array[i]
        gear_indices = np.where(row == gear)[0]

        if len(gear_indices) > 0:
            for gear_index in gear_indices:  # potential bug: assumes no adjacent '*'
                adjacent_numbers = find_numbers_around_gear(array, i, gear_index)
                if len(adjacent_numbers) == 2:
                    ratio = adjacent_numbers[0] * adjacent_numbers[1]
                    cumulative_sum += ratio

    return cumulative_sum


def solve_d3(data_path):
    data = utility.read_file_as_array(data_path)
    q1_answer = get_sum_of_part_numbers(data)
    q2_answer = find_gears(data)

    print('The sum of part numbers is', str(q1_answer))
    print('The sum of all gear ratios is', str(q2_answer))


if __name__ == '__main__':
    path = "/Users/briannavandrey/Desktop/aoc_2023/d3.txt"
    solve_d3(path)