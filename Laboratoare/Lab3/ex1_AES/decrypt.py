from Crypto.Cipher import AES

BLOCK_SIZE = 32
PADDING = b'#'
iv = b'\x00' * 16

def decrypt(key, iv, data):
    return AES.new(key, AES.MODE_CBC, iv).decrypt(data)

with open('secret.enc', 'rb') as f:
    enc = f.read()

key = enc[:BLOCK_SIZE]
cipher = enc[BLOCK_SIZE:]
dec = decrypt(key, iv, cipher).rstrip(PADDING)

with open("decrypted.jpg", 'wb') as out:
    out.write(dec)
