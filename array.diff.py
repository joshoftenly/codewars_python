def array_diff(a, b):
    new_list = []
    for item in a:
        if item not in b:
            new_list.append(item)
    return new_list
