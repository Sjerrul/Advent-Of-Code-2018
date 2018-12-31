from collections import namedtuple
import re


INPUT_PATTERN = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')


class Claim(namedtuple('Claim', 'id x y width height')):
    def __str__(self):
        return "<Claim #{} - {}, {} - {}x{}>".format(self.id, self.x, self.y, self.width, self.height)

    @classmethod
    def from_input(cls, line):
        match = INPUT_PATTERN.match(line)
        if match:
            return cls(*map(int, match.groups()))


def read_file_lines(file_path, strip_lines=True):
    """ Reads the specified file and returns it's lines
        file_path: the path to the file
        strip_lines (default: true): boolean to indicate whether or not to strip leading and trailing whitespace from each line

        Generates the lines in the file as string
    """
    with open(file_path, "r") as f:
        for line in f:
            if strip_lines:
                yield line.strip()
            else:
                yield line


def parse_input(lines):
    return [Claim.from_input(line) for line in lines]


def generate_matrix(size):
    return [[0]*size for _ in range(size)]


def print_matrix(matrix):
    string = '\n'.join(
        'line {}: {}'.format(i, ''.join(map(str, line)))
        for i, line in enumerate(matrix))
    print(string)


if __name__ == '__main__':
    content = read_file_lines("input.txt")
    claims = parse_input(content)

    matrix = generate_matrix(1000)
    for claim in claims:
        x_indexes = range(claim.x, claim.x + claim.width)
        y_indexes = range(claim.y, claim.y + claim.height)

        for x in x_indexes:
            for y in y_indexes:
                matrix[x][y] += 1

    print_matrix(matrix)

    inches_double_claimed = sum(claims > 1 for line in matrix for claims in line)

    print("Inches claimed by two or more claims:", inches_double_claimed)

