import operator

from common import input_parser, utilities as util

from day4.logic.Entry import Entry
from day4.logic.Guard import Guard

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
        if util.contains(guards, lambda g: g.id == entry.guard):
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


max_sleeping_time = 0
most_asleep_minute = None
guard_for_that_minute = None
for g in guards:
    for index, m in enumerate(g.minutes):
        if m >= max_sleeping_time:
            most_asleep_minute = index
            max_sleeping_time = m
            guard_for_that_minute = g

print (max_sleeping_time)
print (most_asleep_minute)
print (guard_for_that_minute)

print("answer:", guard_for_that_minute.id * most_asleep_minute)
