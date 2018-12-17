import sys

from common import input_parser

from day6.logic import calculations
from day6.logic.Matrix import Matrix


if __name__ == '__main__':
    puzzle_input = input_parser.read_file_lines("input.txt")

    coordinates = []
    for line in puzzle_input:
        parts = line.split(", ")
        coordinates.append((int(parts[0]), int(parts[1])))

    limits = calculations.find_limits(coordinates)

    m = Matrix(limits[1][0] + 1, limits[1][1] + 1)

    print("plotting coordinates")
    coordinate_ids = []
    for index, coordinate in enumerate(coordinates):
        print(index, coordinate)
        m.plot_point(index, coordinate)
        coordinate_ids.append(index)

    max_distance = 10000
    region_size = 0
    for x in range(0, m.width):
        for y in range(0, m.height):
            total_distance_to_all = 0
            for index, coordinate in enumerate(coordinates):
                total_distance_to_all += calculations.manhattan_distance((x, y), coordinate)

            if total_distance_to_all <= max_distance:
                region_size += 1


    print(region_size)