import time
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Small message (RSA can only encrypt small data directly)
message = b"RSA Performance Analysis"

key_sizes = [1024, 2048, 4096]

print("=" * 75)
print("{:<10}{:<20}{:<20}{:<20}".format(
    "Key Size", "Key Gen (s)", "Encrypt (s)", "Decrypt (s)"
))
print("=" * 75)

for size in key_sizes:

    # Measure Key Generation Time
    start = time.perf_counter()
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=size
    )
    public_key = private_key.public_key()
    key_time = time.perf_counter() - start

    # Measure Encryption Time
    start = time.perf_counter()
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    enc_time = time.perf_counter() - start

    # Measure Decryption Time
    start = time.perf_counter()
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    dec_time = time.perf_counter() - start

    print("{:<10}{:<20.6f}{:<20.6f}{:<20.6f}".format(
        size, key_time, enc_time, dec_time
    ))

print("=" * 75)
print("Decrypted Message:", plaintext.decode())
