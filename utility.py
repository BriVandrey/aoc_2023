# read in .txt file from specified path
def read_file(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]  # remove new line characters

    return lines
