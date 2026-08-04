from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.exceptions import InvalidSignature

# Generate RSA Keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

# User Input
message = input("Enter the message to sign: ").encode()

# Generate Digital Signature
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("\nDigital Signature Generated Successfully!")
print("Signature (Hex):")
print(signature.hex())

# Verify Original Message
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("\nVerification Successful!")
    print("The signature is VALID.")
except InvalidSignature:
    print("\nVerification Failed!")
    print("The signature is INVALID.")

# Check Modified Message
modified = input("\nEnter a modified message to test (or press Enter to skip): ")

if modified:
    try:
        public_key.verify(
            signature,
            modified.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("Modified message is VALID (Unexpected)")
    except InvalidSignature:
        print("Modified message detected!")
        print("Signature verification FAILED.")
