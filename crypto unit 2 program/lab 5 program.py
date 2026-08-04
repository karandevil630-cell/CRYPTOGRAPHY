from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import time
import os

# DES key (8 bytes)
key = b"ABCDEFGH"

# File sizes
sizes = {
    "1 KB": 1024,
    "10 KB": 10 * 1024,
    "100 KB": 100 * 1024,
    "1 MB": 1024 * 1024
}

print("========== DES Performance Analysis ==========")
print("{:<10} {:<20} {:<20}".format("File Size", "Encryption Time(s)", "Decryption Time(s)"))
print("-" * 55)

for name, size in sizes.items():

    # Create sample file
    filename = "sample.txt"
    with open(filename, "wb") as f:
        f.write(b"A" * size)

    # Read file
    with open(filename, "rb") as f:
        data = f.read()

    cipher = DES.new(key, DES.MODE_ECB)

    # Encryption
    start = time.perf_counter()
    encrypted = cipher.encrypt(pad(data, DES.block_size))
    enc_time = time.perf_counter() - start

    # Save encrypted file
    with open("encrypted.bin", "wb") as f:
        f.write(encrypted)

    # Decryption
    start = time.perf_counter()
    decrypted = unpad(cipher.decrypt(encrypted), DES.block_size)
    dec_time = time.perf_counter() - start

    # Save decrypted file
    with open("decrypted.txt", "wb") as f:
        f.write(decrypted)

    print("{:<10} {:<20.6f} {:<20.6f}".format(name, enc_time, dec_time))

# Remove sample file (optional)
os.remove("sample.txt")
