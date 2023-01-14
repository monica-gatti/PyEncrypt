from Crypto import Random
from Crypto.Cipher import AES

key = b'Sixteen byte key'
iv = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_CFB, iv)
data = b'hello from other side I come from Italy'
print(data)
e_cipher = AES.new(key, AES.MODE_EAX)
e_data = e_cipher.encrypt(data)

d_cipher = AES.new(key, AES.MODE_EAX, e_cipher.nonce)
d_data = d_cipher.decrypt(e_data)

print("Encryption was: ", e_data)
print("Original Message was: ", d_data)