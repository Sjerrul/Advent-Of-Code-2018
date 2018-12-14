def contains(list_, filter_):
    for x in list_:
        if filter_(x):
            return True
    return False


def get_single(list_, filter_):
    return [x for x in list_ if filter_]


def print_items_in_list(list_):
    [print(item) for item in list_]
