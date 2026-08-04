from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import time
import psutil
import os

# Create a sample input file if it doesn't exist
filename = "input.txt"

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("AES Performance Analysis using different key sizes.\n" * 1000)

# Read file data
with open(filename, "rb") as f:
    data = f.read()

# AES key sizes
keys = {
    "128-bit": get_random_bytes(16),
    "192-bit": get_random_bytes(24),
    "256-bit": get_random_bytes(32)
}

process = psutil.Process(os.getpid())

print("=" * 70)
print("{:<10} {:<20} {:<20} {:<15}".format(
    "Key Size", "Encryption Time", "Decryption Time", "Memory (KB)"
))
print("=" * 70)

for key_name, key in keys.items():

    # Memory before encryption
    mem_before = process.memory_info().rss

    # Encryption
    cipher = AES.new(key, AES.MODE_CBC)
    start_enc = time.perf_counter()

    ciphertext = cipher.encrypt(pad(data, AES.block_size))

    enc_time = (time.perf_counter() - start_enc) * 1000

    iv = cipher.iv

    # Decryption
    decipher = AES.new(key, AES.MODE_CBC, iv)

    start_dec = time.perf_counter()

    decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)

    dec_time = (time.perf_counter() - start_dec) * 1000

    # Memory after encryption/decryption
    mem_after = process.memory_info().rss
    memory_used = (mem_after - mem_before) / 1024

    print("{:<10} {:<20.3f} {:<20.3f} {:<15.2f}".format(
        key_name,
        enc_time,
        dec_time,
        memory_used
    ))

print("=" * 70)
