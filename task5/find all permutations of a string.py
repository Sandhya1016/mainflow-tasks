def permute_string(s):
    if len(s) == 0:
        return ['']
    permutations = []
    for i, char in enumerate(s):
        sub_permutations = permute_string(s[:i] + s[i+1:])
        for perm in sub_permutations:
            permutations.append(char + perm)
    return permutations
input_string = input()
print(permute_string(input_string))
