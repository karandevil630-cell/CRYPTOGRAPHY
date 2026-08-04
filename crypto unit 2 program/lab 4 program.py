from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

# DES key (must be the same as used for encryption)
key = b"ABCDEFGH"

# Read encrypted file
with open("encrypted.bin", "rb") as file:
    encrypted_data = file.read()

# Create DES cipher
cipher = DES.new(key, DES.MODE_ECB)

# Decrypt the data
decrypted_data = unpad(cipher.decrypt(encrypted_data), DES.block_size)

# Save decrypted text to a new file
with open("decrypted.txt", "wb") as file:
    file.write(decrypted_data)

print("File decrypted successfully!")
print("Decrypted data saved in 'decrypted.txt'")
