from common import input_parser


class Claim(object):
    id = None
    x = None
    y = None
    width = None
    height = None

    def __init__(self, claim_id, x, y, width, height):
        self.id = claim_id
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __repr__(self):
        return "<Claim #%s - %s, %s - %sx%s>" % (self.id, self.x, self.y, self.width, self.height)


def parse_input(lines):
    claims = []
    for line in lines:
        parts = line.split(" ")

        id = int(parts[0][1:])
        x = int(parts[2].split(",")[0])
        y = int(parts[2].split(",")[1][:-1])
        width = int(parts[3].split("x")[0])
        height = int(parts[3].split("x")[1])

        claims.append(Claim(id, x, y, width, height))

    return claims


def generate_matrix(size):
    return [[0]*size for _ in range(size)]


def print_matrix(matrix):
    print(len(matrix[0]))
    line = ""
    for y in range(0, len(matrix[0])):
        line = line + str(y) + ": "
        for x in range(0, len(matrix[0])):
            line = line + str(matrix[x][y])
        print(line)
        line = ""


content = input_parser.read_file_lines("input.txt")
claims = parse_input(content)

matrix = generate_matrix(1000)
print_matrix(matrix)

for claim in claims:
    x_indexes = range(claim.x, claim.x + claim.width)
    y_indexes = range(claim.y, claim.y + claim.height)

    print(x_indexes)
    print(y_indexes)

    for x in x_indexes:
        for y in y_indexes:
            matrix[x][y] = matrix[x][y] + 1

print_matrix(matrix)

inches_double_claimed = 0
for x in range(0, len(matrix[0])):
    for y in range(0, len(matrix[0])):
        if matrix[x][y] >= 2:
            inches_double_claimed += 1

print("inches claimed by two or more claims", inches_double_claimed)

