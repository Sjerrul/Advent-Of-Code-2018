from common import utilities as util
from day4.logic.Guard import Guard


def parse_entries(entries):
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
                current_guard.minutes[minute_starting_sleep:minute_waking_up] = \
                    [v + 1 for v in current_guard.minutes[minute_starting_sleep:minute_waking_up]]

            if not entry.awake:
                minute_starting_sleep = int(entry.date.strftime("%M"))

    return guards
