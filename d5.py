"""
Q1:
The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.

The rest of the almanac contains a list of maps which describe how to convert numbers from a source category into
numbers in a destination category. That is, the section that starts with seed-to-soil map: describes how to convert a
seed number (the source) to a soil number (the destination). This lets the gardener and his team know which soil to use
with which seeds, which water to use with which fertilizer, and so on.

Rather than list every source number and its corresponding destination number one by one, the maps describe entire
ranges of numbers that can be converted. Each line within a map contains three numbers: the destination range start,
the source range start, and the range length.

The gardener and his team want to get started as soon as possible, so they'd like to know the closest location that
needs a seed. Using these maps, find the lowest location number that corresponds to any of the initial seeds. To do
this, you'll need to convert each seed number through other categories until you can find its corresponding location
number.

What is the lowest location number that corresponds to any of the initial seed numbers?

Q2:
The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and
the second value is the length of the range.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest
location number that corresponds to any of the initial seed numbers?

"""
import re
import utility


def split_into_sections(data):
    sections, section_to_add = [], []
    sections.append(data[0])  # add first line (list of seeds)
    data = data[2:]  # remove first lines from data file

    for line in data:
        if ':' in line:
            if section_to_add:  # progress only if this is not empty
                sections.append(section_to_add[:-1])  # remove blank line at end of section before adding
                section_to_add = []

        else:  # add subsequent lines with no ':' (values)
            section_to_add.append(line)

    if section_to_add:  # add last section after final ':'
        sections.append(section_to_add)

    return sections


def get_number_mapping(number, mapping):
    for map in mapping:
        mappings = re.findall(r'\d+', map)  # three numbers
        destination, origin, range_length = int(mappings[0]), int(mappings[1]), int(mappings[2])
        origin_range = range(origin, origin + range_length + 1)

        if int(number) in origin_range:
            destination_range = range(destination, destination + range_length + 1)
            origin_index = origin_range.index(int(number))  # get index of number in origin range
            number = destination_range[origin_index]  # retrieve destination value
            return number  # return transformed number

    return number  # stays the same if it is not included in the origin range


def get_seed_locations(sections, seeds):
    locations = []

    for seed in seeds:
        current_number = seed
        for i in range(1, len(sections)):
            section = sections[i]  # start from second section
            current_number = get_number_mapping(current_number, section)
        locations.append(current_number)  # this number should now be the location number

    return locations


def find_closest_seed_location_from_pairs(sections, seeds):
    num_pairs = int(len(seeds)/2)
    count = 0
    min_locations = []

    for pair in range(0, num_pairs-1):  # brute force -- VERY COMPUTATIONALLY INTENSIVE
        seed_origin, seed_range = int(seeds[count]), int(seeds[count+1])
        seed_numbers = range(seed_origin, seed_origin + seed_range + 1)
        locations = get_seed_locations(sections, seed_numbers)
        min_locations.append(min(locations))
        count += 2

    return min(min_locations)


def solve_d5(data_path):
    data = utility.read_file(data_path)
    sections = split_into_sections(data)  # split into different mappings
    seeds = re.findall(r'\d+', sections[0].split(':')[1])  # get list of seeds
    q1_answer = get_seed_locations(sections, seeds)
#    q2_answer = find_closest_seed_location_from_pairs(sections, seeds)
    print('Okay gardener, the seed with the nearest location is', str(min(q1_answer)))
#    print(str(q2_answer))


if __name__ == '__main__':
    path = "/Users/briannavandrey/Desktop/aoc_2023/d5.txt"
    solve_d5(path)
