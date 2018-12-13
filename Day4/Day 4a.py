import operator
import datetime
import re

from common import input_parser


class Entry(object):
    date = None
    guard = None
    awake = None

    def __init__(self, line):
        parts = line.split("] ")

        datetime_part = parts[0][1:].split(" ")
        date_parts = datetime_part[0].split("-")
        time_parts = datetime_part[1].split(":")

        self.date = datetime.datetime(int(date_parts[0]), int(date_parts[1]),
                                      int(date_parts[2]), int(time_parts[0]), int(time_parts[1]))

        if "#" in parts[1]:
            self.guard = int(re.search('#(.*) begins', parts[1]).group(1))

        if "asleep" in parts[1]:
            self.awake = False

        if "wakes" in parts[1]:
            self.awake = True

    def __repr__(self):
        return "Entry %s - Guard #%s - status: %s" % (self.date, self.guard, self.awake)


class Guard(object):
    id = None
    minutes = [60]

    def __init__(self, id_):
        self.id = id_
        self.minutes = [0]*60

    def __repr__(self):
        return "<Guard #%s - %s>" % (self.id, self.minutes)

    def get_minutes_sleeping(self):
        return sum(self.minutes)

def contains(list, filter):
    for x in list:
        if filter(x):
            return True
    return False


def get_single(list, filter):
    return [x for x in list if filter]


puzzle_input = input_parser.read_file_lines("input.txt")

entries = []
for line in puzzle_input:
    entries.append(Entry(line))

entries.sort(key=lambda e: e.date)

for e in entries:
    print(e)

guards = []

current_guard = None
minute_starting_sleep = None
minute_waking_up = None

for entry in entries:
    if entry.guard is not None:
        if contains(guards, lambda g: g.id == entry.guard):
            current_guard = [x for x in guards if x.id == entry.guard][0]
            continue
        else:
            guard = Guard(entry.guard)
            guards.append(guard)
            current_guard = guard
            continue

    if entry.awake is not None:
        if entry.awake:
            minute_waking_up = int(entry.date.strftime("%M"))
            print(minute_starting_sleep)
            print(minute_waking_up)
            current_guard.minutes[minute_starting_sleep:minute_waking_up] = [v + 1 for v in current_guard.minutes[minute_starting_sleep:minute_waking_up]]
            print(current_guard.minutes)
        if not entry.awake:
            minute_starting_sleep = int(entry.date.strftime("%M"))

for g in guards:
    print(g)

max_minutes_asleep = 0
most_asleep_guard = None
for g in guards:
    if g.get_minutes_sleeping() > max_minutes_asleep:
        max_minutes_asleep = g.get_minutes_sleeping()
        most_asleep_guard = g

print ("Most asleep guard:", most_asleep_guard)

index, value = max(enumerate(most_asleep_guard.minutes), key=operator.itemgetter(1))
print ("most asleep minute:", index)

print("answer", most_asleep_guard.id * index)