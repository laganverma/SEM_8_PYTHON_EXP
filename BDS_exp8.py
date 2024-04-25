from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

def encrypt_message(key, message):
    # Generate a random initialization vector
    iv = get_random_bytes(AES.block_size)

    # Create AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Pad the message to be a multiple of 16 bytes
    padded_message = message + ((16 - len(message) % 16) * chr(16 - len(message) % 16)).encode()

    # Encrypt the padded message
    ciphertext = cipher.encrypt(padded_message)

    # Combine the IV and ciphertext
    encrypted_message = iv + ciphertext

    return encrypted_message

def decrypt_message(key, encrypted_message):
    # Extract the IV from the encrypted message
    iv = encrypted_message[:AES.block_size]

    # Create AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the ciphertext
    decrypted_message = cipher.decrypt(encrypted_message[AES.block_size:])

    # Remove the padding
    unpadded_message = decrypted_message[:-decrypted_message[-1]]

    return unpadded_message

def main():
    # Secret key (must be 16, 24, or 32 bytes long)
    password = b'my_secret_password'

    # Derive a key from the password
    key = PBKDF2(password, b'salt', 16, count=1000000)

    # Message to encrypt
    message = "Hello, This is a Test Message for this Experiment".encode()

    # Encrypt the message
    encrypted_message = encrypt_message(key, message)
    print("Encrypted:", encrypted_message)

    # Decrypt the message
    decrypted_message = decrypt_message(key, encrypted_message)
    print("Decrypted:", decrypted_message.decode())

if __name__ == "__main__":
    main()
