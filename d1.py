"""
Q1:
As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been
amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are
having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration
value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit
and the last digit (in that order) to form a single two-digit number.

Consider your entire calibration document. What is the sum of all of the calibration values?


Q2:
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two,
three, four, five, six, seven, eight, and nine also count as valid "digits". Equipped with this new information, you
now need to find the real first and last digit on each line.

What is the sum of all of the calibration values?
"""

import re
import utility


def get_first_and_last_numbers(array_of_strings):
    two_digit_numbers = []

    for string in array_of_strings:
        numbers = re.findall(r'\d+', string)  # all numbers
        two_digit_number = numbers[0][0] + numbers[-1][-1]  # concatenate first and last digit
        two_digit_numbers.append(int(two_digit_number))  # add to array as integer
        if len(numbers) == 1:
            print(string,two_digit_number)

    return two_digit_numbers


def convert_strings_to_digits(array_of_strings):
    strings_to_convert = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    # replace with numbers + original strings to handle where number strings overlap
    conversion_values = ['one1one', 'two2two', 'three3three', 'four4four', 'five5five', 'six6six', 'seven7seven',
                         'eight8eight', 'nine9nine']
    converted_data = []

    for string in array_of_strings:
        converted_string = string  # placeholder if no changes needed

        for string_to_convert, conversion_value in zip(strings_to_convert, conversion_values):  # loop through values
            converted_string = converted_string.replace(string_to_convert, conversion_value)  # replace where found

        converted_data.append(converted_string)

    return converted_data


def solve_d1(data_path):
    data = utility.read_file(data_path)
    numbers = get_first_and_last_numbers(data)
    q1_answer = sum(numbers)
    converted_data = convert_strings_to_digits(data)
    q2_numbers = get_first_and_last_numbers(converted_data)
    q2_answer = sum(q2_numbers)

    print('The sum of all calibration values is', str(q1_answer))
    print('The sum of all calibration values after finding the real first and last value is', str(q2_answer))


if __name__ == '__main__':
    path = "/Users/briannavandrey/Desktop/aoc_2023/d1.txt"
    solve_d1(path)

