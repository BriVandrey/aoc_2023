import d1, d2, d3


def happy_christmas():
    print('                            --                            ')
    print('                            --                            ')
    print('On the first day of Christmas, we checked our list of strings...')
    d1.solve_d1(path + 'd1.txt')
    print('                          ------                          ')
    print('                          ------                          ')
    print('On the second day of Christmas, we played a silly cube game...')
    d2.solve_d2(path + 'd2.txt')
    print('                       ------------                        ')
    print('                       ------------                        ')
    print('On the third day of Christmas, we got stuck on a gondola...')
    d3.solve_d3(path + 'd3.txt')



if __name__ == '__main__':
    path = "/Users/briannavandrey/Desktop/aoc_2023/"

