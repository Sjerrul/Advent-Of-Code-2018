def get_most_asleep_guard(guards):

    max_minutes_asleep = 0
    most_asleep_guard = None
    for g in guards:
        if g.get_minutes_sleeping() > max_minutes_asleep:
            max_minutes_asleep = g.get_minutes_sleeping()
            most_asleep_guard = g

    return most_asleep_guard
