import string

from common import input_parser
from day5.logic import catalyser


if __name__ == '__main__':
    polymer = input_parser.read_file_as_string("input.txt")

    reaction_results = dict()

    for letter in string.ascii_lowercase:
        print("Removing", letter)
        cleaned_polymer = catalyser.remove_from_polymer(polymer, letter)

        print("Reacting")
        while True:
            reaction = catalyser.react(cleaned_polymer)
            if reaction[0] == 0:
                break

            cleaned_polymer = reaction[1]

        reaction_results[letter] = reaction

    print("Resulting polymers")
    smallest_length = (None, len(polymer))

    for letter, reaction in reaction_results.items():
        print(letter, reaction)
        if len(reaction[1]) < smallest_length[1]:
            smallest_length = (letter, len(reaction[1]))

    print("Smallest result", smallest_length)

