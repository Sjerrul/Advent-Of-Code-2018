from common import day1
from common import input_parser


frequency_changes = input_parser.read_file_lines_as_int("input.txt")

start_frequency = 0
result = day1.apply_frequency_changes(start_frequency, frequency_changes)

print("Frequency after changes:", result)





