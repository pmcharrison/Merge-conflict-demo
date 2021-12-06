def clean(lst: list):
    lst = remove_excluded(lst)
    return lst

def remove_excluded(lst):
    excluded = ["banana", "orange"]
    return [obj for obj in lst if obj not in excluded]
