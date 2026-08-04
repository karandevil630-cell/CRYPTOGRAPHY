from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad

# Blowfish Key
key = b"SecretKey123"

# Read data from input file
with open("Untitled.txt", "rb") as infile:
    data = infile.read()

# Create Blowfish cipher (ECB mode)
cipher = Blowfish.new(key, Blowfish.MODE_ECB)

# Encrypt the file contents
encrypted_data = cipher.encrypt(pad(data, Blowfish.block_size))

# Save encrypted data
with open("encrypted.bin", "wb") as outfile:
    outfile.write(encrypted_data)

print("========== Blowfish File Encryption ==========")
print("Input File  : Untitled.txt")
print("Output File : encrypted.bin")
print("Encryption Successful!")
