from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Generate RSA private and public keys
private_key=rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key=private_key.public_key()

# Serialize the public key for storage or transmission
public_key_bytes=public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)


# Encrypt data using the public key
def encrypt_data(data,public_key):
    encrypted_data=public_key.encrypt(
        data.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_data


# Decrypt data using the private key
def decrypt_data(encrypted_data,private_key):
    decrypted_data=private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_data.decode()


# Example usage
data_to_encrypt="Lagan Verma, 20BCS3515"
print("Original Data:",data_to_encrypt)

encrypted_data=encrypt_data(data_to_encrypt,public_key)
print("Encrypted:",encrypted_data.hex())

decrypted_data=decrypt_data(encrypted_data,private_key)
print("Decrypted:",decrypted_data)
