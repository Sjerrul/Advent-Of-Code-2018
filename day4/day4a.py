import operator

from common import input_parser, utilities as util

from day4.logic.Entry import Entry
import day4.logic.parser as parser
import day4.logic.analyser as analyser


if __name__ == '__main__':
    puzzle_input = input_parser.read_file_lines("input.txt")

    entries = [Entry(line) for line in puzzle_input]
    entries.sort(key=lambda e: e.date)

    guards = parser.parse_entries(entries)
    util.print_items_in_list(guards)

    most_asleep_guard = analyser.get_most_asleep_guard(guards)

    print("Most asleep guard:", most_asleep_guard)

    index, value = max(enumerate(most_asleep_guard.minutes), key=operator.itemgetter(1))
    print("most asleep minute:", index)
    print("answer", most_asleep_guard.id * index)
