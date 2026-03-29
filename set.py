from exceptions import invalidseterror


def parse_set(s):
    s = s.strip()
    if not s.startswith('{') or not s.endswith('}'):
        raise invalidseterror(f"set must have braces: '{s}'")

    inner = s[1:-1].strip()
    if not inner:
        return set()

    elements = set()
    for item in inner.split(','):
        item = item.strip()
        if not item:
            raise invalidseterror(f"bad set: '{s}'")
        try:
            if '.' in item:
                elements.add(float(item))
            else:
                elements.add(int(item))
        except ValueError:
            elements.add(item)

    return elements


def format_set(s):
    if not s:
        return '{}'
    try:
        sorted_elements = sorted(s, key=lambda x: (isinstance(x, str), x))
    except TypeError:
        sorted_elements = sorted(s, key=str)
    return '{' + ','.join(str(e) for e in sorted_elements) + '}'


def set_union(a, b):
    s1 = parse_set(a)
    s2 = parse_set(b)
    return format_set(s1 | s2)


def set_intersection(a, b):
    s1 = parse_set(a)
    s2 = parse_set(b)
    return format_set(s1 & s2)


def set_difference(a, b):
    s1 = parse_set(a)
    s2 = parse_set(b)
    return format_set(s1 - s2)


def set_symmetric_difference(a, b):
    s1 = parse_set(a)
    s2 = parse_set(b)
    return format_set(s1 ^ s2)


def is_subset(a, b):
    s1 = parse_set(a)
    s2 = parse_set(b)
    return str(s1.issubset(s2))


def is_superset(a, b):
    s1 = parse_set(a)
    s2 = parse_set(b)
    return str(s1.issuperset(s2))
