def read_file_lines(file_path, strip_lines=True):
    """ Reads the specified file and returns it's lines an array
        file_path: the path to the file
        strip_lines (default: true): boolean to indicate whether or not to strip leading and trailing whitespace from each line

        Returns: An array of the lines in the file as string
    """
    with open(file_path, "r") as f:
        if strip_lines:
            return [l.strip() for l in f.readlines()]

        return [l for l in f.readlines()]


def read_file_lines_as_int(file_path):
    lines = read_file_lines(file_path, True)

    values = []
    for value in lines:
        values.append(int(value))

    return values
