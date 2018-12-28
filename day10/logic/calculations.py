def find_limits(coordinates):
    all_x = [coordinate[0] for coordinate in coordinates]
    all_y = [coordinate[1] for coordinate in coordinates]

    return (min(all_x), min(all_y)), (max(all_x), max(all_y))


def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
