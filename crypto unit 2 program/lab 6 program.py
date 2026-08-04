from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad
from binascii import hexlify

# Input
plaintext = "NETWORKSECURITY"
key = b"SecretKey123"

# Create Blowfish cipher (ECB mode)
cipher = Blowfish.new(key, Blowfish.MODE_ECB)

# Blowfish block size is 8 bytes, so pad the plaintext
padded_text = pad(plaintext.encode(), Blowfish.block_size)

# Encrypt
ciphertext = cipher.encrypt(padded_text)

# Display output
print("Plaintext :", plaintext)
print("Key       :", key.decode())
print("Ciphertext (Hex):", hexlify(ciphertext).decode().upper())
