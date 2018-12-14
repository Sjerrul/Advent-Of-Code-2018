import datetime
import re


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
