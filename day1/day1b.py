from common import input_parser
from day1.logic import logic

if __name__ == '__main__':
    frequency_changes = input_parser.read_file_lines_as_int("input.txt")

    starting_frequency = 0
    result = logic.apply_frequency_changes_till_duplicate(starting_frequency, frequency_changes)

    print("Correct frequency:", result)
