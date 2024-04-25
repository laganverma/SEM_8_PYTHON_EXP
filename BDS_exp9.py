from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_message(public_key, message):
    cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

def decrypt_message(private_key, encrypted_message):
    cipher = PKCS1_OAEP.new(RSA.import_key(private_key))
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message

def main():
    # Generate RSA key pair
    private_key, public_key = generate_key_pair()

    # Message to encrypt
    message = "Hello, This is a text message using RSA algorithm"

    # Encrypt the message
    encrypted_message = encrypt_message(public_key, message)
    print("Encrypted:", encrypted_message)

    # Decrypt the message
    decrypted_message = decrypt_message(private_key, encrypted_message)
    print("Decrypted:", decrypted_message)

if __name__ == "__main__":
    main()
