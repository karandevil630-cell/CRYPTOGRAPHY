import time
import secrets

# Prime sizes (bits)
sizes = [128, 256, 512, 1024]

print("Diffie-Hellman Performance Analysis")
print("-" * 60)
print("{:<12}{:<20}".format("Prime Size", "Execution Time (sec)"))
print("-" * 60)

for bits in sizes:

    # Generate a random number with the specified bit length
    p = secrets.randbits(bits)

    # Ensure it is odd
    p |= 1

    g = 5

    # Private keys
    alice_private = secrets.randbelow(10000) + 1
    bob_private = secrets.randbelow(10000) + 1

    # Start timing
    start = time.perf_counter()

    # Public keys
    alice_public = pow(g, alice_private, p)
    bob_public = pow(g, bob_private, p)

    # Shared secret keys
    alice_key = pow(bob_public, alice_private, p)
    bob_key = pow(alice_public, bob_private, p)

    end = time.perf_counter()

    print("{:<12}{:<20.8f}".format(bits, end - start))

print("-" * 60)

if alice_key == bob_key:
    print("Shared Secret Key Verified Successfully!")
else:
    print("Key Exchange Failed!")
