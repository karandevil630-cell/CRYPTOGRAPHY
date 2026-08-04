import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, padding as sympadding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# ---------------- RSA KEY GENERATION ----------------
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

# ---------------- AES SESSION KEY ----------------
aes_key = os.urandom(32)      # 256-bit AES Key
iv = os.urandom(16)           # Initialization Vector

print("AES Session Key Generated Successfully.")

# ---------------- USER MESSAGE ----------------
message = input("Enter Message: ").encode()

# ---------------- AES ENCRYPTION ----------------
padder = sympadding.PKCS7(128).padder()
padded_data = padder.update(message) + padder.finalize()

cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
encryptor = cipher.encryptor()

ciphertext = encryptor.update(padded_data) + encryptor.finalize()

print("\nAES Encrypted Data:")
print(ciphertext.hex())

# ---------------- RSA ENCRYPT AES KEY ----------------
encrypted_key = public_key.encrypt(
    aes_key,
    padding.OAEP(
        mgf=padding.MGF1(hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("\nAES Key Encrypted Using RSA.")

# ---------------- RSA DECRYPT AES KEY ----------------
decrypted_key = private_key.decrypt(
    encrypted_key,
    padding.OAEP(
        mgf=padding.MGF1(hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# ---------------- AES DECRYPTION ----------------
cipher = Cipher(algorithms.AES(decrypted_key), modes.CBC(iv))
decryptor = cipher.decryptor()

decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()

unpadder = sympadding.PKCS7(128).unpadder()
plaintext = unpadder.update(decrypted_padded) + unpadder.finalize()

print("\nRecovered Message:")
print(plaintext.decode())
