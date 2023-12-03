"""
Q1:
To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random
cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). Each game is listed with its ID
number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from
the bag (like 3 red, 5 green, 4 blue).

In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4
red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green
cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration.
However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly,
game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the
games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and
14 blue cubes. What is the sum of the IDs of those games?

Q2:
As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes
of each color that could have been in the bag to make the game possible?

The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the
minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five
powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
"""

import pandas as pd
import re
import utility


def get_game_id(string):
    id_string = string.split(':')[0]
    numbers = re.findall(r'\d+', id_string)
    return int(numbers[0])


def get_number_of_balls(string):
    results = string.split(':')[1]  # remove game ID
    results = results.split(';')  # split into draws
    colors = 'red', 'blue', 'green'
    data = {'color': [], 'number': []}

    for result in results:
        balls = result.split(',')  # split into ball colours

        for ball in balls:
            number = re.findall(r'\d+', ball)  # number (assumes single number)
            color = next((c for c in colors if c.lower() in ball.lower()), None)  # color
            data['color'].append(color)
            data['number'].append(int(number[0]))

    return pd.DataFrame(data)  # return dataframe with filled cols for color and number


def get_max_value(color_string, max_values):
    if color_string == 'red':
        return max_values[0]
    if color_string == 'green':
        return max_values[1]
    if color_string == 'blue':
        return max_values[2]


def check_if_possible(data, max_values):
    colors = 'red', 'blue', 'green'

    for color in colors:
        color_data = data[data['color'] == color]
        max_value = get_max_value(color, max_values)
        result = (color_data['number'] > max_value).any()

        if result:  # if number is > max value for that color, return False
            return False

    return True  # if all numbers =< max value for all colors, return True


def get_possible_games(games):
    possible_games = []
    max_values = [12, 13, 14]  # red, green, blue

    for game in games:
        game_id = get_game_id(game)
        number_of_balls = get_number_of_balls(game)
        is_possible = check_if_possible(number_of_balls, max_values)

        if is_possible:
            possible_games.append(game_id)

    return possible_games


def get_min_values(data):
    colors = 'red', 'blue', 'green'
    min_values = []

    for color in colors:
        color_data = data[data['color'] == color]
        if len(color_data) == 0:
            pass
        else:
            value = (color_data['number']).max()
            min_values.append(value)

    return min_values


def get_powers_of_sets(games):
    powers = []

    for game in games:
        number_of_balls = get_number_of_balls(game)
        min_values = get_min_values(number_of_balls)
        power = min_values[0] * min_values[1] * min_values[2]
        powers.append(power)

    return powers


def solve_d2(data_path):
    data = utility.read_file(data_path)
    possible_games = get_possible_games(data)
    q1_answer = sum(possible_games)
    powers = get_powers_of_sets(data)
    q2_answer = sum(powers)

    print('The sum of all possible game IDs is', str(q1_answer))
    print('The sum of game set powers is', str(q2_answer))


if __name__ == '__main__':
    path = "/Users/briannavandrey/Desktop/aoc_2023/d2.txt"
    solve_d2(path)