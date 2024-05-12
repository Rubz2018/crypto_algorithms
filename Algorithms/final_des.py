# Dependencies : "pip install pycryptodome"

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64

def pad(data):
    block_size = 8
    pad_size = block_size - (len(data) % block_size)
    return data + pad_size.to_bytes(1, byteorder='big') * pad_size

def unpad(data):
    pad_size = data[-1]
    return data[:-pad_size]

def encrypt_des(key, plaintext):
    key = key.ljust(8, ' ')  # DES key must be 8 bytes
    key = key.encode('utf-8')

    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = pad(plaintext.encode('utf-8'))

    ciphertext = cipher.encrypt(plaintext)
    return base64.b64encode(ciphertext).decode('utf-8')

def decrypt_des(key, ciphertext):
    key = key.ljust(8, ' ')  # DES key must be 8 bytes
    key = key.encode('utf-8')

    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = base64.b64decode(ciphertext)

    plaintext = cipher.decrypt(ciphertext)
    return unpad(plaintext).decode('utf-8')

# Example usage:
key = "mysecret"  # 8-character key for DES
plaintext = "Hello, DES encryption and decryption!"

# Encrypt
encrypted_text = encrypt_des(key, plaintext)
print("Encrypted:", encrypted_text)

# Decrypt
decrypted_text = decrypt_des(key, encrypted_text)
print("Decrypted:", decrypted_text)
