from Crypto.PublicKey import RSA
from Crypto.Cipher import PKSC1_OAEP

import base64

pubfile = input('Insert the filename: ')
with open('pubfile', 'rb') as f:
    pub_key = RSA.import_key(f.read())

cipherRsa = PKSC1_OAEP.new(pub_key)    

message = input('Enter a message to encrypt: ')
encrypt_message = cipherRsa.encrypt(message)
print(base64.b64encode(encrypt_message).decode())
    
