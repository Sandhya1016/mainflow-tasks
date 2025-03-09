def find_duplicates(lst):
    duplicates = []
    occurrences = {}
    for item in lst:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1
    for item, count in occurrences.items():
        if count > 1:
            duplicates.append(item)
    return duplicates
input_list = [1, 2, 3, 4, 2, 5, 1, 6, 3]
print(find_duplicates(input_list))
