# Program 1: DES Encryption
# Input: Plaintext = COMPUTER
# Key = A1B2C3D4
# Output: Ciphertext in hexadecimal format

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

# Plaintext and Key
plaintext = "COMPUTER"
key = b"A1B2C3D4"   # DES key must be exactly 8 bytes

# Create DES cipher (ECB mode)
cipher = DES.new(key, DES.MODE_ECB)

# Pad plaintext to multiple of 8 bytes
padded_text = pad(plaintext.encode(), DES.block_size)

# Encrypt
ciphertext = cipher.encrypt(padded_text)

# Display
print("Plaintext :", plaintext)
print("Key       :", key.decode())
print("Ciphertext (Hex):", ciphertext.hex().upper())
