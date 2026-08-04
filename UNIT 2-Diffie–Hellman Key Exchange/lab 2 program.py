# Diffie-Hellman Secure Chat Simulation

# Public values
p = 23
g = 5

# Private keys
alice_private = 6
bob_private = 15

# Public keys
alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)

print("===== DIFFIE-HELLMAN KEY EXCHANGE =====")
print("Prime Number (p):", p)
print("Primitive Root (g):", g)

print("\nAlice Public Key:", alice_public)
print("Bob Public Key:", bob_public)

# Shared Secret Keys
alice_key = pow(bob_public, alice_private, p)
bob_key = pow(alice_public, bob_private, p)

print("\nAlice Shared Secret Key:", alice_key)
print("Bob Shared Secret Key:", bob_key)

if alice_key == bob_key:
    print("\nShared Secret Key Established Successfully!")
else:
    print("\nKey Exchange Failed!")

# Alice sends message
message = input("\nAlice: ")

# Encrypt
encrypted = ""
for ch in message:
    encrypted += chr(ord(ch) ^ alice_key)

print("\nEncrypted Message:", encrypted)

# Bob decrypts
decrypted = ""
for ch in encrypted:
    decrypted += chr(ord(ch) ^ bob_key)

print("\nBob Received:", decrypted)

# Bob replies
reply = input("\nBob: ")

# Encrypt reply
encrypted_reply = ""
for ch in reply:
    encrypted_reply += chr(ord(ch) ^ bob_key)

print("\nEncrypted Reply:", encrypted_reply)

# Alice decrypts
decrypted_reply = ""
for ch in encrypted_reply:
    decrypted_reply += chr(ord(ch) ^ alice_key)

print("\nAlice Received:", decrypted_reply)
