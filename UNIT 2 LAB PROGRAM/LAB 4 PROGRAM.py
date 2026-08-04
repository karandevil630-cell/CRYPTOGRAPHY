from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os

# -----------------------------
# Select AES Key Size
# -----------------------------
print("Choose AES Key Size")
print("1. AES-128")
print("2. AES-192")
print("3. AES-256")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    key = get_random_bytes(16)      # 128-bit
elif choice == "2":
    key = get_random_bytes(24)      # 192-bit
elif choice == "3":
    key = get_random_bytes(32)      # 256-bit
else:
    print("Invalid choice!")
    exit()

print("\nGenerated Key (Hex):")
print(key.hex())

# -----------------------------
# Enter File Name
# -----------------------------
filename = input("\nEnter file name (Example: sample.txt or sample.pdf): ")

if not os.path.exists(filename):
    print("File not found!")
    exit()

# Read original file
with open(filename, "rb") as f:
    data = f.read()

# -----------------------------
# Encrypt File
# -----------------------------
cipher = AES.new(key, AES.MODE_CBC)

ciphertext = cipher.encrypt(pad(data, AES.block_size))

encrypted_file = filename + ".enc"

with open(encrypted_file, "wb") as f:
    f.write(cipher.iv)
    f.write(ciphertext)

print("\nFile Encrypted Successfully!")
print("Encrypted File:", encrypted_file)

# -----------------------------
# Decrypt File
# -----------------------------
with open(encrypted_file, "rb") as f:
    iv = f.read(16)
    encrypted_data = f.read()

decipher = AES.new(key, AES.MODE_CBC, iv)

decrypted_data = unpad(decipher.decrypt(encrypted_data), AES.block_size)

decrypted_file = "decrypted_" + filename

with open(decrypted_file, "wb") as f:
    f.write(decrypted_data)

print("File Decrypted Successfully!")
print("Decrypted File:", decrypted_file)

# -----------------------------
# Verify
# -----------------------------
with open(filename, "rb") as f:
    original = f.read()

with open(decrypted_file, "rb") as f:
    recovered = f.read()

if original == recovered:
    print("\nVerification: SUCCESS")
    print("Recovered file matches the original.")
else:
    print("\nVerification: FAILED")
    print("Recovered file does not match the original.")
