def encrypt_message(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                encrypted_message += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_message += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_message += char
    return encrypted_message

def decrypt_message(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                decrypted_message += chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
            else:
                decrypted_message += chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
        else:
            decrypted_message += char
    return decrypted_message
message = input("Enter a message to encrypt: ")
key = int(input("Enter the encryption key (integer): "))
encrypted_message = encrypt_message(message, key)
print(f"Encrypted message: {encrypted_message}")

decrypted_message = decrypt_message(encrypted_message, key)
print(f"Decrypted message: {decrypted_message}")
