import random
from math import gcd

# Function to find modular inverse
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

# Step 1: Choose two prime numbers
p = int(input("Enter first prime number (p): "))
q = int(input("Enter second prime number (q): "))

# Step 2: Calculate n and phi
n = p * q
phi = (p - 1) * (q - 1)

# Step 3: Choose e
e = 2
while e < phi:
    if gcd(e, phi) == 1:
        break
    e += 1

# Step 4: Calculate d
d = mod_inverse(e, phi)

print("\nGenerated Keys")
print("Public Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))

# Step 5: Input message
message = input("\nEnter plaintext message: ")

# Step 6: Encrypt
cipher = []
for ch in message:
    cipher.append(pow(ord(ch), e, n))

print("Encrypted Ciphertext:")
print(cipher)

# Step 7: Decrypt
decrypted = ""
for c in cipher:
    decrypted += chr(pow(c, d, n))

print("Decrypted Message:", decrypted)
