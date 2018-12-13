from collections import defaultdict

import itertools

from common import input_parser


def get_difference_count(item1, item2):
    difference = 0
    for index, char in enumerate(item1):
        if item2[index] != char:
            difference += 1
    return difference


boxIds = input_parser.read_file_lines("input.txt")

differenceScores = defaultdict()
for a, b in itertools.combinations(boxIds, 2):
    differenceScores[a, b] = get_difference_count(a, b)

indexOfLowestDifference = min(differenceScores, key=differenceScores.get)

print("Most similar", indexOfLowestDifference, differenceScores[indexOfLowestDifference])

end_result = ""

for index, char in enumerate(indexOfLowestDifference[0]):
    print("comparing", indexOfLowestDifference[1][index], char )
    if indexOfLowestDifference[1][index] == char:
        end_result = end_result + char

print("endResult:", end_result)

