import re

from day10.logic import calculations

class Star:
    x: int = None
    y: int = None
    vx: int = None
    vy: int = None

    def __init__(self, x, y, vx, vy):
        self.x = int(x)
        self.y = int(y)
        self.vx = int(vx)
        self.vy = int(vy)

    def __repr__(self):
        return "<Star %s,%s - velocity: %s,%s>" % (self.x, self.y, self.vx, self.vy)

def width_of_stars(stars):
    all_y = [coordinate[1] for coordinate in [(s.x, s.y) for s in stars]]
    return max(all_y) - min(all_y)

def tick(stars):
    for s in stars:
        s.x += s.vx
        s.y += s.vy

    return stars

def visualize(stars):
    grid = [[' '] * 400 for j in range(100, 300)]
    for s in stars:
        grid[s.y][s.x] = '#'

    for row in grid:
        print(''.join(row))

if __name__ == '__main__':
    star_information = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            line = line.replace(" ", "")
            groups = re.search('position=<(.*),(.*)>velocity=<(.*),(.*)>', line)
            star_information.append(Star(groups.group(1), groups.group(2), groups.group(3), groups.group(4)))

    for star in star_information:
        print(star)

    star_information = tick(star_information)
    current_tick = 0
    smallest_width = width_of_stars(star_information)

    max_tick = 10644
    while current_tick < max_tick:
        star_information = tick(star_information)
        current_width = width_of_stars(star_information)
        if current_width <= smallest_width:
            smallest_width = current_width
            print(smallest_width)
            current_tick += 1
        else:
            break;

    visualize(star_information)
