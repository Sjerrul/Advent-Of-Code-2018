import numpy as np

from common import input_parser


frequency_changes = input_parser.read_file_lines_as_int("input.txt")

frequency = 0
frequencies_seen = np.empty(0, dtype=np.int)

frequency_seen = False
while not frequency_seen:
    frequency += frequency_changes[0]
    if frequency in frequencies_seen:
        frequency_seen = True
    else:
        frequencies_seen = np.append(frequencies_seen, frequency)
        frequency_changes = np.roll(frequency_changes, -1)

print(frequency)
