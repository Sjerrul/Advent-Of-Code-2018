def read_file_lines(filename):
    with open(filename, "r") as f:
        return [l.strip() for l in f.readlines()]
