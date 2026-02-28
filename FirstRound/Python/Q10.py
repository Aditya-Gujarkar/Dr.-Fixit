#You try to use a set comprehension to deduplicate pairs, but see a TypeError:
pairs = [([1, 2], 3), ([1, 2], 3)]
unique = {p for p in pairs}

