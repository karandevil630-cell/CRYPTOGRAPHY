# Diffie-Hellman Key Exchange with Multiple Users

# Public values
p = 23
g = 5

print("===== Diffie-Hellman Multiple Users =====")
print("Prime Number (p):", p)
print("Primitive Root (g):", g)

# Number of users
n = int(input("\nEnter the number of users: "))

private_keys = []
public_keys = []

# Input private keys and generate public keys
for i in range(n):
    private = int(input(f"Enter Private Key for User {i+1}: "))
    private_keys.append(private)

    public = pow(g, private, p)
    public_keys.append(public)

# Display public keys
print("\nPublic Keys")
for i in range(n):
    print(f"User {i+1}: {public_keys[i]}")

# Select two users
u1 = int(input("\nEnter First User Number: ")) - 1
u2 = int(input("Enter Second User Number: ")) - 1

# Generate shared keys
key1 = pow(public_keys[u2], private_keys[u1], p)
key2 = pow(public_keys[u1], private_keys[u2], p)

print("\nShared Secret Key computed by User", u1 + 1, ":", key1)
print("Shared Secret Key computed by User", u2 + 1, ":", key2)

# Verification
if key1 == key2:
    print("\nSecure Key Established Successfully!")
else:
    print("\nKey Exchange Failed!")
