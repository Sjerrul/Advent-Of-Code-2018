import numpy


def apply_frequency_changes(frequency, frequency_changes):
    """ Applies a list of frequency changes to a starting frequency

        frequency: the frequency to start with
        frequency_changes: the list of changes to apply
    """
    for change in frequency_changes:
        frequency += change

    return frequency


def apply_frequency_changes_till_duplicate(frequency, frequency_changes):
    frequencies_seen = numpy.empty(0, dtype=numpy.int)

    frequency_seen = False
    while not frequency_seen:
        frequency += frequency_changes[0]
        if frequency in frequencies_seen:
            frequency_seen = True
        else:
            frequencies_seen = numpy.append(frequencies_seen, frequency)
            frequency_changes = numpy.roll(frequency_changes, -1)

    return frequency
