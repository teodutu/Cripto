import argparse
from Crypto.Cipher import AES
from Crypto.Util import Counter

BLOCK_SIZE = 32

def bytexor(a, b):  # xor two byte strings (trims the longer input)
	return b"".join([bytes([x ^ y]) for (x, y) in zip(a, b)])

def decrypt_cbc(key, ciphertext):
	iv = bytes.fromhex(ciphertext[:BLOCK_SIZE])
	encrypted_text = bytes.fromhex(ciphertext[BLOCK_SIZE:])

	cipher = AES.new(bytes.fromhex(key), AES.MODE_CBC, iv)
	plaintext = cipher.decrypt(encrypted_text)
	padding = plaintext[-1]

	return plaintext[:-padding].decode("ASCII")

def decrypt_ctr(key, ciphertext):
	iv = bytes.fromhex(ciphertext[:BLOCK_SIZE])
	encrypted_text = bytes.fromhex(ciphertext[BLOCK_SIZE:])

	cnt = Counter.new(BLOCK_SIZE * 4, initial_value=int(iv.hex(), 16))
	cipher = AES.new(bytes.fromhex(key), AES.MODE_CTR, counter=cnt)
	plaintext = cipher.decrypt(encrypted_text)
	return plaintext.decode("ASCII")

def decrypt_cbc_manual(key, ciphertext):
	ciphertext_blocks = [bytes.fromhex(ciphertext[i:i + BLOCK_SIZE])
		for i in range(0, len(ciphertext), BLOCK_SIZE)]

	cipher = AES.new(bytes.fromhex(key), AES.MODE_ECB)
	plaintext = b""

	for i in range(1, len(ciphertext_blocks)):
		decrypted_block = cipher.decrypt(ciphertext_blocks[i])
		plaintext += bytexor(ciphertext_blocks[i - 1], decrypted_block)

	padding = plaintext[-1]

	return plaintext[:-padding].decode("ASCII")

def decrypt_ctr_manual(key, ciphertext):
	ciphertext_blocks = [bytes.fromhex(ciphertext[i:i + BLOCK_SIZE])
		for i in range(0, len(ciphertext), BLOCK_SIZE)]
	iv = ciphertext_blocks[0]

	cipher = AES.new(bytes.fromhex(key), AES.MODE_ECB)
	plaintext = b""

	for i in range(1, len(ciphertext_blocks)):
		decrypted_iv = cipher.encrypt(iv)
		plaintext += bytexor(ciphertext_blocks[i], decrypted_iv)

		next_iv_int = int.from_bytes(iv, byteorder="big") + 1
		iv = next_iv_int.to_bytes(16, "big")

	return plaintext.decode("ASCII")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Decrypts an AES-enctypted " +
		"message either using CBC or CTR.")
	parser.add_argument("-m", "--mode", type=str, choices=["cbc", "ctr"],
		dest="mode", required=True, help="The encryption mode used for AES")
	parser.add_argument("-k", "--key", type=str, dest="key", required=True,
		help="The key used for encryption")
	parser.add_argument("-c", "--ciphertext", type=str, dest="ciphertext",
		required=True, help="The cipher text to be decrypted")
	args = parser.parse_args()

	plaintext = ""
	if args.mode == "cbc":
		plaintext = decrypt_cbc_manual(args.key, args.ciphertext)
	else:
		plaintext = decrypt_ctr_manual(args.key, args.ciphertext)

	print(plaintext)
