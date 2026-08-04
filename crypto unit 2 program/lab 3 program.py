Ufrom Crypto.Cipher import DES
from Crypto.Util.Padding import pad

# DES key (8 bytes)
key = b"ABCDEFGH"

# Ask user for file name
filename = input("Enter the text file name: ")

# Read the file
file = open(filename, "rb")
data = file.read()
file.close()

# Encrypt
cipher = DES.new(key, DES.MODE_ECB)
encrypted = cipher.encrypt(pad(data, 8))

# Save encrypted data
file = open("encrypted.bin", "wb")
file.write(encrypted)
file.close()

print("File encrypted successfully!")
print("Encrypted file saved as encrypted.bin")
