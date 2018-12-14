def react(polymer):
    reactions_done = 0
    pointer = 0

    new_polymer = ""
    while pointer < len(polymer) - 1:
        unit = polymer[pointer]
        next_unit = polymer[pointer+1]

        if unit != next_unit and unit.upper() == next_unit.upper() and unit.lower() == next_unit.lower():
            pointer = pointer + 2
            reactions_done += 1
        else:
            new_polymer += unit
            pointer = pointer + 1

    if pointer == len(polymer) - 1:
        new_polymer += polymer[pointer]

    return reactions_done, new_polymer


def remove_from_polymer(polymer: str, char):
    return polymer.replace(char.upper(), "").replace(char.lower(), "")
