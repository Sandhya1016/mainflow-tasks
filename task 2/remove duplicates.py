def remove_duplicates(lst):
    unique_list = []
    seen = set()
    for item in lst:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list
example_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(example_list)
print(f"The list with duplicates removed is {unique_list}.")
