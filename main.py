import d1, d2, d3, d4, d5


def happy_christmas(path):
    print('                            *                             ')
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
    print('                    ------------------                     ')
    print('                    ------------------                     ')
    print('On the fourth day of Christmas, we played the lottery...')
    d4.solve_d4(path + 'd4.txt')
    print('                --------------------------                 ')
    print('                --------------------------                 ')
    print('On the fifth day of Christmas, we came to realise we are crap gardeners...')
    d5.solve_d5(path + 'd5.txt')
    print('           ------------------------------------            ')
    print('           -XX--XX--XX--XX--XX--XX--XX--XX--XX-            ')
    print('           ------------------------------------            ')





if __name__ == '__main__':
    path = "/Users/briannavandrey/Desktop/aoc_2023/"
    happy_christmas(path)

