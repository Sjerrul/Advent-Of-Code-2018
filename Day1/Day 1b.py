import numpy as np
import common

content = common.read_file_lines("input.txt")

frequencyChanges = []
for value in content:
    frequencyChanges.append(int(value))

frequency = 0
seenFrequencies = []
print("starting...")
frequencySeen = False;
loops = 0
while not frequencySeen:
    frequency += frequencyChanges[0]
    if frequency in seenFrequencies:
        frequencySeen = True
    else:     
        seenFrequencies.append(frequency)
        frequencyChanges = np.roll(frequencyChanges, -1)
    loops += 1
    
print(frequency)
print(loops)

