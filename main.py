def clean(x: list):
    x = remove_excluded(x)
    x = add_none(x)
    return x

def remove_excluded(x):
    excluded = ["banana", "orange"]
    return [obj for obj in x if obj not in excluded]

def add_none(x):
    if None not in x:
        x = x + [None]
    return x
