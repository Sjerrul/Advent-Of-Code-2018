from day1.logic import logic
from common import input_parser


if __name__ == '__main__':
    frequency_changes = input_parser.read_file_lines_as_int("input.txt")

    start_frequency = 0
    result = logic.apply_frequency_changes(start_frequency, frequency_changes)

    print("Frequency after changes:", result)





