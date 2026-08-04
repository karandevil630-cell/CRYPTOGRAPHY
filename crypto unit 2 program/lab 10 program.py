from Crypto.Cipher import DES, Blowfish
from Crypto.Util.Padding import pad, unpad
import time
import tracemalloc

# Keys
des_key = b"ABCDEFGH"
blowfish_key = b"SecretKey123"

# File sizes
sizes = {
    "1 KB": 1024,
    "10 KB": 10 * 1024,
    "100 KB": 100 * 1024,
    "1 MB": 1024 * 1024
}

print("=" * 90)
print("{:<8} {:<10} {:<12} {:<12} {:<12} {:<12}".format(
    "Size", "Algorithm", "Enc Time", "Dec Time", "Memory", "Cipher Size"))
print("=" * 90)

for name, size in sizes.items():

    # Create sample data
    data = b"A" * size

    # ---------- DES ----------
    des = DES.new(des_key, DES.MODE_ECB)

    tracemalloc.start()

    start = time.perf_counter()
    des_cipher = des.encrypt(pad(data, DES.block_size))
    enc_time = time.perf_counter() - start

    start = time.perf_counter()
    des_plain = unpad(des.decrypt(des_cipher), DES.block_size)
    dec_time = time.perf_counter() - start

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("{:<8} {:<10} {:<12.6f} {:<12.6f} {:<12} {:<12}".format(
        name, "DES", enc_time, dec_time, str(peak) + " B", len(des_cipher)))

    # ---------- Blowfish ----------
    blowfish = Blowfish.new(blowfish_key, Blowfish.MODE_ECB)

    tracemalloc.start()

    start = time.perf_counter()
    bf_cipher = blowfish.encrypt(pad(data, Blowfish.block_size))
    enc_time = time.perf_counter() - start

    start = time.perf_counter()
    bf_plain = unpad(blowfish.decrypt(bf_cipher), Blowfish.block_size)
    dec_time = time.perf_counter() - start

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("{:<8} {:<10} {:<12.6f} {:<12.6f} {:<12} {:<12}".format(
        "", "Blowfish", enc_time, dec_time, str(peak) + " B", len(bf_cipher)))

    print("-" * 90)
