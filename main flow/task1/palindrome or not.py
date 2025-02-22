def is_palindrome(s):
    cleaned_string = ''.join(filter(str.isalnum, s)).lower()
    return cleaned_string == cleaned_string[::-1]
word = input("Enter a word: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")
