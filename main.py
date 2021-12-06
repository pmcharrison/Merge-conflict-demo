def clean(x: list):
    x = remove_excluded(x)
    return x

def remove_excluded(x):
    excluded = ["banana", "orange"]
    return [obj for obj in x if obj not in excluded]
