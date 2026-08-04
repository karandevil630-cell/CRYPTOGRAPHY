from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import unpad

# Blowfish Key (same key used for encryption)
key = b"SecretKey123"

# Read encrypted file
with open("encrypted.bin", "rb") as infile:
    encrypted_data = infile.read()

# Create Blowfish cipher
cipher = Blowfish.new(key, Blowfish.MODE_ECB)

# Decrypt the data
decrypted_data = unpad(cipher.decrypt(encrypted_data), Blowfish.block_size)

# Save decrypted data
with open("decrypted.txt", "wb") as outfile:
    outfile.write(decrypted_data)

print("========== Blowfish File Decryption ==========")
print("Encrypted File : encrypted.bin")
print("Output File    : decrypted.txt")
print("Decryption Successful!")

# Verify the decrypted file matches the original
with open("Untitled.txt", "rb") as original:
    original_data = original.read()

if original_data == decrypted_data:
    print("Verification: SUCCESS")
    print("The decrypted content matches the original file.")
else:
    print("Verification: FAILED")
    print("The decrypted content does not match the original file.")

