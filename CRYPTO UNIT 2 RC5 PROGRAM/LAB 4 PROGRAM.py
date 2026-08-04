# RC5 File Encryption and Decryption

import struct

# RC5 Parameters
WORD_SIZE = 32
ROUNDS = 12
BLOCK_SIZE = 8
MASK = 0xFFFFFFFF


# RC5 Key Expansion
def rc5_key_expansion(key):
    P = 0xB7E15163
    Q = 0x9E3779B9

    key_words = []
    for i in range(0, len(key), 4):
        key_words.append(int.from_bytes(key[i:i+4], 'little'))

    S = [P]
    for i in range(1, 2 * ROUNDS + 2):
        S.append((S[i-1] + Q) & MASK)

    i = j = 0
    A = B = 0

    for _ in range(3 * len(S)):
        A = S[i] = ((S[i] + A + B) & MASK)
        A = ((A << 3) | (A >> (WORD_SIZE-3))) & MASK

        B = key_words[j] = ((key_words[j] + A + B) & MASK)
        B = ((B << ((A+B) % WORD_SIZE)) |
             (B >> (WORD_SIZE - ((A+B) % WORD_SIZE)))) & MASK

        i = (i + 1) % len(S)
        j = (j + 1) % len(key_words)

    return S


def left_rotate(x, y):
    y %= WORD_SIZE
    return ((x << y) | (x >> (WORD_SIZE-y))) & MASK


def right_rotate(x, y):
    y %= WORD_SIZE
    return ((x >> y) | (x << (WORD_SIZE-y))) & MASK


# RC5 Encryption
def rc5_encrypt(block, S):
    A, B = struct.unpack("<II", block)

    A = (A + S[0]) & MASK
    B = (B + S[1]) & MASK

    for i in range(1, ROUNDS+1):
        A = (left_rotate(A ^ B, B) + S[2*i]) & MASK
        B = (left_rotate(B ^ A, A) + S[2*i+1]) & MASK

    return struct.pack("<II", A, B)


# RC5 Decryption
def rc5_decrypt(block, S):
    A, B = struct.unpack("<II", block)

    for i in range(ROUNDS, 0, -1):
        B = right_rotate((B - S[2*i+1]) & MASK, A) ^ A
        A = right_rotate((A - S[2*i]) & MASK, B) ^ B

    B = (B - S[1]) & MASK
    A = (A - S[0]) & MASK

    return struct.pack("<II", A, B)


# File Encryption
def encrypt_file(input_file, output_file, key):
    with open(input_file, "rb") as f:
        data = f.read()

    # Padding
    while len(data) % BLOCK_SIZE != 0:
        data += b'\0'

    S = rc5_key_expansion(key)

    encrypted = b''

    for i in range(0, len(data), BLOCK_SIZE):
        encrypted += rc5_encrypt(data[i:i+BLOCK_SIZE], S)

    with open(output_file, "wb") as f:
        f.write(encrypted)


# File Decryption
def decrypt_file(input_file, output_file, key):
    with open(input_file, "rb") as f:
        data = f.read()

    S = rc5_key_expansion(key)

    decrypted = b''

    for i in range(0, len(data), BLOCK_SIZE):
        decrypted += rc5_decrypt(data[i:i+BLOCK_SIZE], S)

    decrypted = decrypted.rstrip(b'\0')

    with open(output_file, "wb") as f:
        f.write(decrypted)


# Main Program

key = b"SecretKey1234567"

original = "original.txt"
encrypted = "encrypted.rc5"
decrypted = "decrypted.txt"


encrypt_file(original, encrypted, key)

decrypt_file(encrypted, decrypted, key)


# Verification

with open(original, "rb") as f1:
    original_data = f1.read()

with open(decrypted, "rb") as f2:
    decrypted_data = f2.read()


print("Original File  :", original)
print("Encrypted File :", encrypted)
print("Decrypted File :", decrypted)

if original_data == decrypted_data:
    print("Verification   : Successful")
    print("Decrypted file is identical to original file")
else:
    print("Verification   : Failed")
