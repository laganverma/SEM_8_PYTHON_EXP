from Crypto.Util import number

def generate_dh_params():
    # Generate a large prime number p and a primitive root g
    p = number.getPrime(128)
    g = 2  # Primitive root for simplicity
    return p, g

def generate_private_key(p):
    # Generate a random private key that's less than p
    private_key = number.getRandomRange(2, p - 1)
    return private_key

def compute_public_key(g, private_key, p):
    # Calculate public_key = g^private_key mod p
    public_key = pow(g, private_key, p)
    return public_key

def compute_shared_secret(public_key, private_key, p):
    # Calculate shared secret = public_key^private_key mod p
    shared_secret = pow(public_key, private_key, p)
    return shared_secret

# Generate DH parameters (p and g)
p, g = generate_dh_params()

# Generate private keys for Alice and Bob
private_key_a = generate_private_key(p)
private_key_b = generate_private_key(p)

# Compute public keys
public_key_a = compute_public_key(g, private_key_a, p)
public_key_b = compute_public_key(g, private_key_b, p)

# Compute the shared secret
shared_secret_a = compute_shared_secret(public_key_b, private_key_a, p)
shared_secret_b = compute_shared_secret(public_key_a, private_key_b, p)

# Output the results
print("Ianur's Shared Secret:", shared_secret_a)
print("Alam's Shared Secret:", shared_secret_b)
