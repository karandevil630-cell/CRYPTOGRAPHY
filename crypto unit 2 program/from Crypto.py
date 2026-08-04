from Crypto.Cipher import DES
from binascii import unhexlify

# Key and ciphertext (hexadecimal)
key = unhexlify("133457799BBCDFF1")
ciphertext = unhexlify("85E813540F0AB405")

# Create DES cipher in ECB mode
des = DES.new(key, DES.MODE_ECB)

# Decrypt the ciphertext
plaintext = des.decrypt(ciphertext)

# Display the result
print("Ciphertext :", "85E813540F0AB405")
print("Key        :", "133457799BBCDFF1")
print("Plaintext (Hex)  :", plaintext.hex().upper())

# Convert plaintext to ASCII (if printable)
try:
    print("Plaintext (ASCII):", plaintext.decode())
except UnicodeDecodeError:
    print("Plaintext (ASCII): Not printable")