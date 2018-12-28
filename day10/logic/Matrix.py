class Matrix:
    width = None
    height = None
    grid = None

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[-1] * self.height for _ in range(self.width)]

    def print(self, use_char=False):
        line = ""
        for y in range(0, len(self.grid[0])):
            line = line + str(y) + ": "
            for x in range(0, len(self.grid)):
                char_to_use = self.grid[x][y]
                if use_char:
                    char_to_use = chr(65 + self.grid[x][y])
                line = line + str(char_to_use)
            print(line)
            line = ""

    def plot_point(self, point_name, coordinate):
        self.grid[coordinate[0]][coordinate[1]] = point_name

