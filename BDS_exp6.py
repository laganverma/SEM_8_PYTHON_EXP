def caesar_cipher_encrypt(text,shift):
    encrypted_text=""
    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper=char.isupper()

            # Shift the character by the specified amount
            char_code=ord(char)
            encrypted_char_code=(char_code-ord('A' if is_upper else 'a')+shift)%26
            encrypted_char=chr(encrypted_char_code+ord('A' if is_upper else 'a'))

            encrypted_text+=encrypted_char
        else:
            # If the character is not a letter, keep it unchanged
            encrypted_text+=char

    return encrypted_text


def caesar_cipher_decrypt(text,shift):
    return caesar_cipher_encrypt(text,-shift)


# Example usage:
plaintext="Hello, World!"
shift_amount=3

# Encryption
encrypted_text=caesar_cipher_encrypt(plaintext,shift_amount)
print("Encrypted:",encrypted_text)

# Decryption
decrypted_text=caesar_cipher_decrypt(encrypted_text,shift_amount)
print("Decrypted:",decrypted_text)