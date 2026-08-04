import struct
import time

# Circular Left Rotation
def rol(x, y, w):
    return ((x << (y % w)) & ((1 << w) - 1)) | (x >> (w - (y % w)))

# Circular Right Rotation
def ror(x, y, w):
    return (x >> (y % w)) | ((x << (w - (y % w))) & ((1 << w) - 1))

# RC5 Key Expansion
def key_expansion(key, w, r):
    Pw = 0xB7E15163
    Qw = 0x9E3779B9

    u = w // 8
    c = max(1, len(key) // u)

    L = [0] * c
    for i in range(len(key) - 1, -1, -1):
        L[i // u] = (L[i // u] << 8) + key[i]

    t = 2 * (r + 1)
    S = [0] * t
    S[0] = Pw

    for i in range(1, t):
        S[i] = (S[i - 1] + Qw) & 0xFFFFFFFF

    A = B = i = j = 0

    for k in range(3 * max(t, c)):
        A = S[i] = rol((S[i] + A + B) & 0xFFFFFFFF, 3, w)
        B = L[j] = rol((L[j] + A + B) & 0xFFFFFFFF, (A + B), w)

        i = (i + 1) % t
        j = (j + 1) % c

    return S

# RC5 Encryption
def rc5_encrypt(pt, S, w, r):
    A, B = struct.unpack("<2I", pt)

    A = (A + S[0]) & 0xFFFFFFFF
    B = (B + S[1]) & 0xFFFFFFFF

    for i in range(1, r + 1):
        A = (rol(A ^ B, B, w) + S[2 * i]) & 0xFFFFFFFF
        B = (rol(B ^ A, A, w) + S[2 * i + 1]) & 0xFFFFFFFF

    return struct.pack("<2I", A, B)

# RC5 Decryption
def rc5_decrypt(ct, S, w, r):
    A, B = struct.unpack("<2I", ct)

    for i in range(r, 0, -1):
        B = ror((B - S[2 * i + 1]) & 0xFFFFFFFF, A, w) ^ A
        A = ror((A - S[2 * i]) & 0xFFFFFFFF, B, w) ^ B

    B = (B - S[1]) & 0xFFFFFFFF
    A = (A - S[0]) & 0xFFFFFFFF

    return struct.pack("<2I", A, B)

# ---------------- Main Program ----------------

plaintext = input("Enter 8-character plaintext: ")
plaintext = plaintext.ljust(8)[:8]

key = input("Enter Secret Key: ").encode()

w = 32
rounds_list = [8, 12, 16, 20]

print("\nPerformance Analysis of RC5")
print("=" * 60)
print("{:<18} {:<20} {:<20}".format(
    "Rounds", "Encryption(ms)", "Decryption(ms)"))
print("=" * 60)

for r in rounds_list:

    S = key_expansion(key, w, r)

    start = time.perf_counter()
    cipher = rc5_encrypt(plaintext.encode(), S, w, r)
    enc_time = (time.perf_counter() - start) * 1000

    start = time.perf_counter()
    rc5_decrypt(cipher, S, w, r)
    dec_time = (time.perf_counter() - start) * 1000

    print("{:<18} {:<20.4f} {:<20.4f}".format(
        r, enc_time, dec_time))
