from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Generate RSA Keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

# Read plaintext from file
with open("input.txt", "rb") as f:
    plaintext = f.read()

print("Original Text:")
print(plaintext.decode())

# Encrypt
ciphertext = public_key.encrypt(
    plaintext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Store encrypted data
with open("encrypted.bin", "wb") as f:
    f.write(ciphertext)

print("\nCiphertext stored in encrypted.bin")

# Read encrypted data
with open("encrypted.bin", "rb") as f:
    encrypted_data = f.read()

# Decrypt
decrypted = private_key.decrypt(
    encrypted_data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Store decrypted text
with open("decrypted.txt", "wb") as f:
    f.write(decrypted)

print("\nDecrypted Text:")
print(decrypted.decode())

print("\nDecrypted text saved to decrypted.txt")
