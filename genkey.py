from Crypto.PublicKey import RSA

key = RSA.generate(2048)
priv = key.export_key()
with open('private.pem', 'wb') as f:
    f.write(priv)
