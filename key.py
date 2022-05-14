from Crypto import Random
from Crypto.PublicKey import RSA
import base64

def generate_keys():
	modulus_length = 256*4
	privatekey = RSA.generate(modulus_length)
	publickey = privatekey.publickey()

	return privatekey, publickey

def veri_sifrele(data , publickey):
	encrypted_data = publickey.encrypt(data, 32)[0]
	encoded_encrypted_data = base64.b64encode(encrypted_data)
	return encoded_encrypted_data

def veri_coz(encoded_encrypted_data, privatekey):
	decoded_encrypted_data = base64.b64decode(encoded_encrypted_data)
	decoded_decrypted_data = privatekey.decrypt(decoded_encrypted_data)
	return decoded_decrypted_data

private_key, public_key = generate_keys()
pr_file = open("./private_key", "wb")
pr_file.write(private_key)
pr_file.close()
pb_file = open("./public_key", "wb")
pb_file.write(public_key)
pb_file.close()