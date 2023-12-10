import numpy as np
import pandas as pd

# read in .txt file from specified path as a list
def read_file(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]  # remove new line characters

    return lines


# read in .txt file from specified path as a numpy array
def read_file_as_array(path):
    lines = read_file(path)
    data_array = np.array([list(line) for line in lines], dtype='U1')  # format as 2d array

    return data_array

