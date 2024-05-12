from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64
import binascii

def add_padding (text, blocksize =64):
    pad_len = blocksize - (len(text) % blocksize)
    padding = '$' * pad_len
    return text + padding

def remove_padding(text, blocksize=64):
    counter = 0

    for c in text[::-1]:
        if c == '$':
            counter += 1
        else:
            break

    return text[:-counter]



def encrypt(plain_text, key):
    des = DES.new(key.encode('utf-8'), DES.MODE_CBC, iv=get_random_bytes(8))
    padded_text = add_padding(plain_text)
    cipher_text = des.encrypt(padded_text.encode('utf-8'))
    return binascii.hexlify(cipher_text).decode('utf-8')

def decrypt(cipher_text, key):
    des = DES.new(key.encode('utf-8'), DES.MODE_CBC, iv=get_random_bytes(8))
    cipher_text = binascii.unhexlify(cipher_text)
    decrypted_bytes = des.decrypt(cipher_text)
    return decrypted_bytes
if __name__  == '__main__': 
    key = 'secretaa'
    plain_text = 'This is the secret message we want to encrypt!fdf'
    cipher_text = encrypt(plain_text, key)
    print("Encrypted:", cipher_text)
    decrypted_bytes = decrypt(cipher_text, key)    
    decrypted_text = remove_padding(decrypted_bytes.decode('utf-8'))
    print("Decrypted:", decrypted_text)
         


    

     