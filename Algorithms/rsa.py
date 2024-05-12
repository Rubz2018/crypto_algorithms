import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal.")

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # Use Euclid's Algorithm to generate the private key
    d = mod_inverse(e, phi)
    
    # Return public and private key pair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt(public_key, plaintext):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

# Example usage
if __name__ == "__main__":
    p = 61
    q = 53
    public, private = generate_keypair(p, q)
    print("Public Key:", public)
    print("Private Key:", private)

    message = "Hello, RSA!"
    print("Original Message:", message)

    encrypted_message = encrypt(public, message)
    print("Encrypted Message:", encrypted_message)

    decrypted_message = decrypt(private, encrypted_message)
    print("Decrypted Message:", decrypted_message)
