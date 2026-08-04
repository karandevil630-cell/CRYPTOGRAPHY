# Diffie-Hellman MITM Attack Simulation

# Public values
p = 23
g = 5

# Private Keys
alice_private = 6
bob_private = 15
eve_private = 13

print("========== NORMAL DIFFIE-HELLMAN ==========")

# Public Keys
alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)

print("Alice Public Key:", alice_public)
print("Bob Public Key:", bob_public)

# Shared Keys
alice_key = pow(bob_public, alice_private, p)
bob_key = pow(alice_public, bob_private, p)

print("\nAlice Shared Key:", alice_key)
print("Bob Shared Key:", bob_key)

if alice_key == bob_key:
    print("\nSecure Communication Established.")
else:
    print("\nKey Exchange Failed.")

print("\n==========================================")
print("      MAN-IN-THE-MIDDLE ATTACK")
print("==========================================")

# Eve's Public Key
eve_public = pow(g, eve_private, p)

print("Eve intercepts the communication!")
print("Eve Public Key:", eve_public)

# Alice thinks Eve's key is Bob's
alice_fake_key = pow(eve_public, alice_private, p)

# Bob thinks Eve's key is Alice's
bob_fake_key = pow(eve_public, bob_private, p)

# Eve computes both keys
eve_key_with_alice = pow(alice_public, eve_private, p)
eve_key_with_bob = pow(bob_public, eve_private, p)

print("\nAlice's Key (with Eve):", alice_fake_key)
print("Bob's Key (with Eve):", bob_fake_key)

print("Eve's Key with Alice:", eve_key_with_alice)
print("Eve's Key with Bob:", eve_key_with_bob)

print("\nResult:")
print("Alice believes she shares a key with Bob.")
print("Bob believes he shares a key with Alice.")
print("Actually, both communicate through Eve.")

print("\n==========================================")
print(" AUTHENTICATED KEY EXCHANGE")
print("==========================================")

print("Alice verifies Bob's Public Key.")
print("Bob verifies Alice's Public Key.")
print("Eve cannot replace the public keys.")

print("\nAuthenticated Shared Key:", alice_key)
print("Communication is Secure.")

print("\n========== COMPARISON ==========")
print("Normal Exchange       : Secure")
print("MITM Attack           : Compromised")
print("Authenticated Exchange: Secure")
