def to_bytes(value, unit):
    check = {'B': 0, 'KB': 1, 'MB': 2, 'GB': 3}
    return value * (1024 ** check[unit])


def in_largest_units(value):
    i = 0
    units = ["B", "KB", "MB", "GB"]
    while value >= 1024:
        value /= 1024
        i += 1
    return '{} {}'.format(value, units[i])