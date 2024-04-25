def substitution_cipher(text, key, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if encrypt:
        return ''.join(key[alphabet.index(c)] if c in alphabet else c for c in text.lower()).capitalize()
    else:
        return ''.join(alphabet[key.index(c.lower())] if c.lower() in key else c for c in text)

key = 'zyxwvutsrqponmlkjihgfedcba'
plaintext = "This is Experiment Seven of BDS"
encrypted_text = substitution_cipher(plaintext, key)
decrypted_text = substitution_cipher(encrypted_text, key, encrypt=False)

print("Original Text:", plaintext)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
