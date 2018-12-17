from common import input_parser

from day5.logic import catalyser


if __name__ == '__main__':
    polymer = input_parser.read_file_as_string("input.txt")

    reaction = None
    while True:
        reaction = catalyser.react(polymer)
        if reaction[0] == 0:
            break

        polymer = reaction[1]

    print("End result polymer:", polymer)
    print("Final reaction:", reaction)
    print("Answer (length of remaining polymer):", len(polymer))
