from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

# Function to ensure the key is exactly 16 bytes (128 bits)
def format_key(key):
    key = key.encode('utf-8')
    if len(key) < 16:
        key = key.ljust(16, b' ')
    else:
        key = key[:16]
    return key

# Accept plaintext and key from the user
plaintext = input("Enter Plaintext: ")
key = input("Enter 16-character Secret Key: ")

# Format the key
key = format_key(key)

# Create AES cipher (ECB mode)
cipher = AES.new(key, AES.MODE_ECB)

# Encrypt
ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))

print("\nEncrypted Ciphertext (Hex):")
print(binascii.hexlify(ciphertext).decode())

# Decrypt
decipher = AES.new(key, AES.MODE_ECB)
decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)

print("\nDecrypted Text:")
print(decrypted.decode())

# Verification
if decrypted.decode() == plaintext:
    print("\nVerification Successful: Decrypted text matches the original plaintext.")
else:
    print("\nVerification Failed!")
