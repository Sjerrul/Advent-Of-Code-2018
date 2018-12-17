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

    print("calculating closest plotted point")
    for x in range(0, m.width):
        for y in range(0, m.height):
            closest_coordinate = None
            closest_distance = sys.maxsize

            for index, coordinate in enumerate(coordinates):
                distance_to_coordinate = calculations.manhattan_distance((x, y), coordinate)
                if distance_to_coordinate < closest_distance:
                    closest_distance = distance_to_coordinate
                    closest_coordinate = index

                    m.plot_point(closest_coordinate, (x, y))
                elif distance_to_coordinate == closest_distance:
                    m.plot_point(-2, (x, y))


    m.print(True)

    print("removing edge coordinates from possibility list")
    print(coordinate_ids)
    for x in range(0, m.width):
        for y in range(0, m.height):
            if (x == 0 or x == m.width - 1 or y == 0 or y == m.height - 1) and (m.grid[x][y] in coordinate_ids):
                coordinate_ids.remove(m.grid[x][y])

    print("leftover possibilities:", coordinate_ids)
    print("number of leftover possibilties:", len(coordinate_ids))

    print("calculating areas")
    areas = dict()
    for x in range(0, m.width):
        for y in range(0, m.height):
            if m.grid[x][y] in coordinate_ids:
                if m.grid[x][y] not in areas:
                    areas[m.grid[x][y]] = 1
                else:
                    areas[m.grid[x][y]] += 1

    for a in areas:
        print(a, areas[a])
