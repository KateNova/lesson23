from flask import abort


def lines(filename):
    with open(filename, encoding='utf-8') as file:
        for line in file:
            yield line


def limit(iterable, value):
    counter = 0
    it = iter(iterable)
    value = int(value)
    while counter < value:
        yield next(it)
        counter += 1


def unique(iterable, *args):
    return [k for k in {k: None for k in iterable}]


def xfilter(iterable, value):
    return filter(lambda x: True if value in x else False, iterable)


def sort(iterable, value):
    if value == 'asc':
        return sorted(iterable)
    elif value == 'desc':
        return sorted(iterable, reverse=True)
    else:
        abort(400)


def xmap(iterable, value):
    return map(lambda item: item.split()[int(value)], iterable)
