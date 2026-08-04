from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Function to count changed bits
def count_changed_bits(data1, data2):
    count = 0
    for b1, b2 in zip(data1, data2):
        count += bin(b1 ^ b2).count("1")
    return count

# 16-byte AES-128 key
key = b"1234567890ABCDEF"

# Original plaintext (16 bytes)
plaintext = bytearray(b"HELLOAESWORLD12")

# Encrypt original plaintext
cipher1 = AES.new(key, AES.MODE_ECB)
ciphertext1 = cipher1.encrypt(pad(bytes(plaintext), AES.block_size))

# Change one bit in the plaintext
modified_plaintext = bytearray(plaintext)
modified_plaintext[0] ^= 0x01      # Flip the least significant bit of first byte

# Encrypt modified plaintext
cipher2 = AES.new(key, AES.MODE_ECB)
ciphertext2 = cipher2.encrypt(pad(bytes(modified_plaintext), AES.block_size))

# Compare ciphertexts
changed_bits = count_changed_bits(ciphertext1, ciphertext2)
total_bits = len(ciphertext1) * 8
percentage = (changed_bits / total_bits) * 100

# Display results
print("Original Plaintext :", plaintext.decode())
print("Modified Plaintext :", modified_plaintext)

print("\nCiphertext 1 :", ciphertext1.hex())
print("Ciphertext 2 :", ciphertext2.hex())

print("\nTotal Bits in Ciphertext :", total_bits)
print("Changed Bits            :", changed_bits)
print("Avalanche Effect        : {:.2f}%".format(percentage))
