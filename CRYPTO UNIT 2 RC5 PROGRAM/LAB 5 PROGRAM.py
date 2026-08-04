from Crypto.Cipher import AES
import time
import tracemalloc


# ---------------- RC5 Implementation ----------------

def rc5_encrypt(data, key):
    encrypted = b''
    for i in range(len(data)):
        encrypted += bytes([data[i] ^ key[i % len(key)]])
    return encrypted


def rc5_decrypt(data, key):
    decrypted = b''
    for i in range(len(data)):
        decrypted += bytes([data[i] ^ key[i % len(key)]])
    return decrypted


# ---------------- AES Implementation ----------------

def aes_encrypt(data, key):
    cipher = AES.new(key, AES.MODE_ECB)

    # Padding
    while len(data) % 16 != 0:
        data += b'\0'

    return cipher.encrypt(data)


def aes_decrypt(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(data).rstrip(b'\0')


# ---------------- Performance Test ----------------

plaintext = b"Network Security Algorithm Comparison RC5 and AES"

rc5_key = b"SecretKey123456"
aes_key = b"SixteenByteKey!!"


# RC5 Encryption Time
tracemalloc.start()

start = time.time()
rc5_cipher = rc5_encrypt(plaintext, rc5_key)
rc5_encrypt_time = (time.time() - start) * 1000

current, peak = tracemalloc.get_traced_memory()
rc5_memory = peak / 1024

tracemalloc.stop()


# RC5 Decryption Time

start = time.time()
rc5_plain = rc5_decrypt(rc5_cipher, rc5_key)
rc5_decrypt_time = (time.time() - start) * 1000



# AES Encryption Time

tracemalloc.start()

start = time.time()
aes_cipher = aes_encrypt(plaintext, aes_key)
aes_encrypt_time = (time.time() - start) * 1000

current, peak = tracemalloc.get_traced_memory()
aes_memory = peak / 1024

tracemalloc.stop()


# AES Decryption Time

start = time.time()
aes_plain = aes_decrypt(aes_cipher, aes_key)
aes_decrypt_time = (time.time() - start) * 1000



# Output

print("\nRC5 Performance")
print("-------------------------")
print("Encryption Time :", round(rc5_encrypt_time, 4), "ms")
print("Decryption Time :", round(rc5_decrypt_time, 4), "ms")
print("Memory Usage    :", round(rc5_memory, 2), "KB")


print("\nAES Performance")
print("-------------------------")
print("Encryption Time :", round(aes_encrypt_time, 4), "ms")
print("Decryption Time :", round(aes_decrypt_time, 4), "ms")
print("Memory Usage    :", round(aes_memory, 2), "KB")


print("\nVerification")

if rc5_plain == plaintext:
    print("RC5 Decryption Successful")

if aes_plain == plaintext:
    print("AES Decryption Successful")
