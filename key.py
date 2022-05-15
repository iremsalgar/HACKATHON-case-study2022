# from Crypto import Random
# from Crypto.PublicKey import RSA
# import base64

# def generate_keys():
# 	modulus_length = 256*8
# 	privatekey = RSA.generate(modulus_length, Random.new().read)
# 	publickey = privatekey.publickey()

# 	return privatekey, publickey

# def veri_sifrele(data , publickey):
# 	i = 0
# 	encrypted_data = b''
# 	while 1:
# 		encrypted_data += publickey.encrypt(data[i:i+180])
# 		i+=180
# 		if i + 180 > len(data):
# 			encoded_encrypted_data = base64.b64encode(encrypted_data)
# 			print(len(encoded_encrypted_data))
# 			# if len(encoded_encrypted_data) > 345":
# 			# 	veri_sifrele(encoded_encrypted_dat"a, publickey)
# 			return encoded_encrypted_data

# def veri_coz(encoded_encrypted_data, privatekey):
# 	decoded_encrypted_data = base64.b64decode(encoded_encrypted_data)
# 	decoded_decrypted_data = privatekey.decrypt(decoded_encrypted_data)
# 	return decoded_decrypted_data

# private_key, public_key = generate_keys()
# pr_file = open("./private_key.pem", "wb")
# pr_file.write((private_key).exportKey())
# pr_file.close()
# pb_file = open("./public_key.pem", "wb")
# pb_file.write(public_key.exportKey())
# pb_file.close()