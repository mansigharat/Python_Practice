data = [[1,2],[3,[4,5],[6]]]

def flatten(seq):
    """Return a flattened copy of seq (list of nested lists)."""
    out = []
    for item in seq:
        if isinstance(item, list):
            out.extend(flatten(item))
        else:
            out.append(item)
    return out

print(flatten(data))