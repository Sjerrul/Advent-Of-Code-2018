def apply_frequency_changes(frequency, frequency_changes):
    """ Applies a list of frequency changes to a starting frequency

        frequency: the frequency to start with
        frequency_changes: the list of changes to apply
    """
    for change in frequency_changes:
        frequency += change

    return frequency


