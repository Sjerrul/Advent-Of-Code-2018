from collections import defaultdict

from common import input_parser


if __name__ == '__main__':
    boxIds = input_parser.read_file_lines("input.txt")

    parsedBoxIds = []

    for boxId in boxIds:
        characters = defaultdict(int)
        for char in boxId:
            characters[char] += 1

        parsedBoxIds.append(characters)

    idsWith2Letters = 0
    idsWith3Letters = 0

    for parsedBoxId in parsedBoxIds:
        if 2 in parsedBoxId.values():
            idsWith2Letters += 1
        if 3 in parsedBoxId.values():
            idsWith3Letters += 1

    print("result:", idsWith2Letters * idsWith3Letters)