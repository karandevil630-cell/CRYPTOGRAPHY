from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util import Counter
import time

# Read sample data
filename = "input.txt"

try:
    with open(filename, "rb") as f:
        data = f.read()
except:
    data = b"This is a sample text for AES Modes Comparison." * 100

# AES-128 Key
key = get_random_bytes(16)

results = []

# ---------------- ECB ----------------
cipher = AES.new(key, AES.MODE_ECB)
start = time.perf_counter()
ciphertext = cipher.encrypt(pad(data, AES.block_size))
enc_time = (time.perf_counter() - start) * 1000

results.append([
    "ECB",
    enc_time,
    ciphertext[:32].hex(),
    "One block error affects only that block",
    "Least Secure"
])

# ---------------- CBC ----------------
cipher = AES.new(key, AES.MODE_CBC)
start = time.perf_counter()
ciphertext = cipher.encrypt(pad(data, AES.block_size))
enc_time = (time.perf_counter() - start) * 1000

results.append([
    "CBC",
    enc_time,
    ciphertext[:32].hex(),
    "One block affects current and next block",
    "High Security"
])

# ---------------- CFB ----------------
cipher = AES.new(key, AES.MODE_CFB)
start = time.perf_counter()
ciphertext = cipher.encrypt(data)
enc_time = (time.perf_counter() - start) * 1000

results.append([
    "CFB",
    enc_time,
    ciphertext[:32].hex(),
    "Bit error affects current and next segment",
    "High Security"
])

# ---------------- OFB ----------------
cipher = AES.new(key, AES.MODE_OFB)
start = time.perf_counter()
ciphertext = cipher.encrypt(data)
enc_time = (time.perf_counter() - start) * 1000

results.append([
    "OFB",
    enc_time,
    ciphertext[:32].hex(),
    "Bit error affects only corresponding bit",
    "Very High Security"
])

# ---------------- CTR ----------------
ctr = Counter.new(128)
cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
start = time.perf_counter()
ciphertext = cipher.encrypt(data)
enc_time = (time.perf_counter() - start) * 1000

results.append([
    "CTR",
    enc_time,
    ciphertext[:32].hex(),
    "Bit error affects only corresponding bit",
    "Excellent Security"
])

# ---------------- Display ----------------
print("=" * 120)
print("{:<8} {:<18} {:<40} {:<35} {:<15}".format(
    "Mode",
    "Encryption(ms)",
    "Ciphertext Pattern",
    "Error Propagation",
    "Security"
))
print("=" * 120)

for r in results:
    print("{:<8} {:<18.3f} {:<40} {:<35} {:<15}".format(
        r[0], r[1], r[2], r[3], r[4]
    ))

print("=" * 120)
