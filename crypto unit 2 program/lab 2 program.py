from Crypto.Cipher import DES

# Convert hexadecimal string to bytes
ciphertext = bytes.fromhex("85E813540F0AB405")
key = bytes.fromhex("133457799BBCDFF1")

# Create DES cipher (ECB mode)
cipher = DES.new(key, DES.MODE_ECB)

# Decrypt
plaintext = cipher.decrypt(ciphertext)

# Display results
print("Ciphertext :", ciphertext.hex().upper())
print("Key        :", key.hex().upper())
print("Plaintext (Hex):", plaintext.hex().upper())

# Try to display as ASCII (if printable)
try:
    print("Plaintext (ASCII):", plaintext.decode())
except UnicodeDecodeError:
    print("Plaintext contains non-printable ASCII characters.")
