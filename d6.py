"""
Q1:
The organizer brings you over to the area where the boat races are held. The boats are much smaller than you expected
- they're actually toy boats, each with a big button on top. Holding down the button charges the boat, and releasing
the button allows the boat to move. Boats move faster if their button was held longer, but time spent holding the
button counts against the total race time. You can only hold the button at the start of the race, and boats don't move
until the button is released.

To see how much margin of error you have, determine the number of ways you can beat the record in each race; in this
example, if you multiply these values together, you get 288 (4 * 8 * 9).

Determine the number of ways you could beat the record in each race. What do you get if you multiply these numbers
together?

Q2:
There's really only one race - ignore the spaces between the numbers on each line. How many ways can you beat the
record in this one much longer race?
"""

import re
import utility


def find_possible_ways(time, record):
    count = 0
    for i in range(0, time+1):
        distance = i * (time - i)  # travelled distance (i = speed per ms)
        if distance > record:
            count += 1
    return count


def how_to_beat_the_records(times, distances):
    result = 1  # to store cumulative result
    for time, distance in zip(times, distances):
        num_ways = find_possible_ways(int(time), int(distance))
        result = result * num_ways  # multiply result by number of ways
    return result


def solve_d6(data_path):
    data = utility.read_file(data_path)
    times, distances = re.findall(r'\d+', data[0]), re.findall(r'\d+', data[1])  # length of race: ms, distance: mm
    q1_answer = how_to_beat_the_records(times, distances)
    q2_answer = find_possible_ways(int(''.join(times)), int(''.join(distances)))

    print('We multiplied our possible wins to get', str(q1_answer), '! Why you ask? No idea.')
    print('But if we calculated the possibilities for one race, we found there were', q2_answer)


if __name__ == '__main__':
    path = "/Users/briannavandrey/Desktop/aoc_2023/d6.txt"
    solve_d6(path)