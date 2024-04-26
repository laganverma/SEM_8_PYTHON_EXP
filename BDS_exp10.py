from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Generate parameters for the key exchange
parameters = dh.generate_parameters(generator=2, key_size=2048)
private_key_a = parameters.generate_private_key()
private_key_b = parameters.generate_private_key()

# Get the public parts of the keys
public_key_a = private_key_a.public_key()
public_key_b = private_key_b.public_key()

# Serialize public keys to send to each other
serialized_public_key_a = public_key_a.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
serialized_public_key_b = public_key_b.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Deserialize received public keys
received_public_key_a = serialization.load_pem_public_key(
    serialized_public_key_b,
    backend=default_backend()
)
received_public_key_b = serialization.load_pem_public_key(
    serialized_public_key_a,
    backend=default_backend()
)

# Perform the key exchange
shared_key_a = private_key_a.exchange(received_public_key_a)
shared_key_b = private_key_b.exchange(received_public_key_b)

# Output the results
print("Lagan's Shared Secret:", shared_key_a.hex())
print("Verma's Shared Secret:", shared_key_b.hex())
