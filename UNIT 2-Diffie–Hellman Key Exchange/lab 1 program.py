# Diffie-Hellman Key Exchange Algorithm

# Input public values
p = int(input("Enter Prime Number (p): "))
g = int(input("Enter Primitive Root (g): "))

# Input private keys
alice_private = int(input("Enter Alice's Private Key: "))
bob_private = int(input("Enter Bob's Private Key: "))

# Generate public keys
alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)

print("\nAlice's Public Key =", alice_public)
print("Bob's Public Key =", bob_public)

# Compute shared secret keys
alice_shared = pow(bob_public, alice_private, p)
bob_shared = pow(alice_public, bob_private, p)

print("\nAlice's Shared Secret Key =", alice_shared)
print("Bob's Shared Secret Key =", bob_shared)

# Verify
if alice_shared == bob_shared:
    print("\nKey Exchange Successful!")
    print("Shared Secret Key =", alice_shared)
else:
    print("\nKey Exchange Failed!")
