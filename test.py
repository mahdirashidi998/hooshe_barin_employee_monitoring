def remove_duplicates(dicts):
    seen = set()
    unique_dicts = []
    for d in dicts:
        # Convert dictionary to a tuple of sorted key-value pairs
        tuple_repr = tuple(sorted(d.items()))
        if tuple_repr not in seen:
            seen.add(tuple_repr)
            unique_dicts.append(d)
    return unique_dicts

d=[{'x': 538, 'y': 82, 'w': 83, 'h': 170, 'color': (0, 128, 0)}, 
   {'x': 538, 'y': 82, 'w': 83, 'h': 170, 'color': (0, 128, 0)},
   {'x': 49, 'y': 46, 'w': 115, 'h': 245, 'color': (255, 0, 0)},
   {'x': 575, 'y': 35, 'w': 115, 'h': 245, 'color': (255, 0, 0)}]

print(remove_duplicates(d))