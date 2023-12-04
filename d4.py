"""
Q1:
The Elf leads you over to the pile of colorful cards. There, you discover dozens of scratchcards, all with their opaque
covering already scratched off. Picking one up, it looks like each card has two lists of numbers separated by a vertical
bar (|): a list of winning numbers and then a list of numbers you have. You organize the information into a table (your
puzzle input).

As far as the Elf has been able to figure out, you have to figure out which of the numbers you have appear in the list
of winning numbers. The first match makes the card worth one point and each match after the first doubles the point
value of that card.

Take a seat in the large pile of colorful cards. How many points are they worth in total?

Q2:

"""

import numpy as np
import re
import utility


def count_winning_numbers(string):
    line = string.split(':')[1]  # remove card ID
    winning_numbers = re.findall(r'\d+', line.split('|')[0])
    our_numbers = re.findall(r'\d+', line.split('|')[1])
    num_winners = len(set(winning_numbers) & set(our_numbers))  # numbers that appear in both

    return num_winners


def calculate_points(num):
    points = 0
    if num > 0:
        points = 1
        for i in range(num-1):
            points = points * 2

    return points


def get_number_of_points(strings):
    points = []

    for line in strings:
        num_winners = count_winning_numbers(line)
        num_points = calculate_points(num_winners)  # calculate number of points
        points.append(num_points)

    return sum(points)


def update_card_counts(card, counts, num_winners):
    for i in range(card, card+num_winners):
        counts[i] += 1

    return counts


def count_scratchcards(data):
    current_card = 1
    card_counts = np.ones(len(data))  # start with one of each card

    for line in data:
        num_repeats = int(card_counts[current_card-1])
        num_winners = count_winning_numbers(line)
        for i in range(num_repeats):
            card_counts = update_card_counts(current_card, card_counts, num_winners)
        current_card += 1  # move on to the next card(s)

    return int(sum(card_counts))


def solve_d4(data_path):
    data = utility.read_file(data_path)
    q1_answer = get_number_of_points(data)
    q2_answer = count_scratchcards(data)

    print('This elf has lottery cards that are worth', str(q1_answer), 'points in total! Wow!')
    print('Nope - hang on. This elf has', str(q2_answer), 'scratchcards in total!')


if __name__ == '__main__':
    path = "/Users/briannavandrey/Desktop/aoc_2023/d4.txt"
    solve_d4(path)