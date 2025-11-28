def flatten_iterate(sequence):
    for item in sequence:
        if isinstance(item, list):
            for x in flatten_iterate(item):
                yield x
        else:
            yield item