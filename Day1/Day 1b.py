import numpy as np

import common

content = common.read_file_lines("input.txt")

frequencyChanges = []
for value in content:
    frequencyChanges.append(int(value))

frequency = 0
seenFrequencies = dict()
print("starting...")
frequencySeen = False

while not frequencySeen:
    frequency += frequencyChanges[0]
    if frequency in seenFrequencies:
        frequencySeen = True
    else:
        seenFrequencies[frequency] = 1
        frequencyChanges = np.roll(frequencyChanges, -1)
    
print(frequency)

