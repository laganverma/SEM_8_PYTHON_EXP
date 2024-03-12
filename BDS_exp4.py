from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct

def decrypt_message(iv, ct, key):
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ct)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')

# Example usage
key = get_random_bytes(16)  # Generate a random 16 bytes key
message = "Hello, this is a secret message!"
print("Original Message:", message)

iv, ciphertext = encrypt_message(message, key)
print("Encrypted Message:", ciphertext)

decrypted_message = decrypt_message(iv, ciphertext, key)
print("Decrypted Message:", decrypted_message)