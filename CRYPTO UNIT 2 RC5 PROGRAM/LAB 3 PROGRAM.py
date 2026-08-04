import struct

# ---------------- RC5 Functions ----------------

def rol(x, y, w):
    return ((x << (y % w)) & ((1 << w) - 1)) | (x >> (w - (y % w)))

def ror(x, y, w):
    return (x >> (y % w)) | ((x << (w - (y % w))) & ((1 << w) - 1))

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

def rc5_encrypt(pt, S, w, r):
    A, B = struct.unpack("<2I", pt)

    A = (A + S[0]) & 0xFFFFFFFF
    B = (B + S[1]) & 0xFFFFFFFF

    for i in range(1, r + 1):
        A = (rol(A ^ B, B, w) + S[2 * i]) & 0xFFFFFFFF
        B = (rol(B ^ A, A, w) + S[2 * i + 1]) & 0xFFFFFFFF

    return struct.pack("<2I", A, B)

# Function to count changed bits
def count_changed_bits(c1, c2):
    count = 0
    for b1, b2 in zip(c1, c2):
        count += bin(b1 ^ b2).count("1")
    return count

# ---------------- Main Program ----------------

plaintext = input("Enter 8-character plaintext: ")
plaintext = plaintext.ljust(8)[:8]

key = input("Enter Secret Key: ").encode()

w = 32
r = 12

S = key_expansion(key, w, r)

# Encrypt original plaintext
cipher1 = rc5_encrypt(plaintext.encode(), S, w, r)

# Modify one bit of the plaintext
modified = bytearray(plaintext.encode())
modified[0] ^= 0x01        # Flip one bit in the first character

# Encrypt modified plaintext
cipher2 = rc5_encrypt(bytes(modified), S, w, r)

# Calculate avalanche effect
changed_bits = count_changed_bits(cipher1, cipher2)
total_bits = len(cipher1) * 8
percentage = (changed_bits / total_bits) * 100

# Display results
print("\nOriginal Plaintext :", plaintext)
print("Modified Plaintext :", modified.decode(errors="ignore"))

print("\nOriginal Ciphertext :", cipher1.hex().upper())
print("Modified Ciphertext :", cipher2.hex().upper())

print("\nChanged Bits Count :", changed_bits)
print("Avalanche Percentage : {:.2f}%".format(percentage))
