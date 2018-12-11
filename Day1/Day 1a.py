import common

content = common.read_file_lines("input.txt")

frequencyChanges = []
for value in content:
    frequencyChanges.append(int(value))

frequency = 0
for change in frequencyChanges:
    frequency += change

print("Frequency after changes:", frequency)
