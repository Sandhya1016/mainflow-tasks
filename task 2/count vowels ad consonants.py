def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in s:
        if char.isalpha():  
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count
example_string = "Hello, world!"
vowels, consonants = count_vowels_consonants(example_string)
print(f"The string '{example_string}' has {vowels} vowels and {consonants} consonants.")
