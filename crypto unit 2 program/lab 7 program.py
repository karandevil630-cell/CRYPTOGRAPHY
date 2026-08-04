from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad

# Input
plaintext = "NETWORKSECURITY"
key = b"SecretKey123"

# Create Blowfish cipher (ECB Mode)
cipher = Blowfish.new(key, Blowfish.MODE_ECB)

# Blowfish block size = 8 bytes
plaintext_bytes = pad(plaintext.encode(), Blowfish.block_size)

# Encrypt
ciphertext = cipher.encrypt(plaintext_bytes)

# Display Output
print("========== Blowfish Encryption ==========")
print("Plaintext :", plaintext)
print("Key       :", key.decode())
print("Ciphertext (Hex):", ciphertext.hex().upper())
