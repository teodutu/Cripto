def hexxor(a, b):  # xor two hex strings (trims the longer input)
	ha = bytes.fromhex(a)
	hb = bytes.fromhex(b)
	return "".join(["{:02x}".format(x ^ y) for (x, y) in zip(ha, hb)])

def main():
	# Plaintexts
	s1 = "floare"
	s2 = "albina"
	crc1 = "8e31"  # CRC-16 of x1
	crc2 = "54ba"  # CRC-16 of x2

	initial_cipher = "021e0e061d1694c9"

	# Obtain crc of s1
	# See this site:
	# http://www.lammertbies.nl/comm/info/crc-calculation.html
	x1 = s1.encode().hex()
	x2 = s2.encode().hex()

	print("x1 + crc1: " + x1 + crc1)
	print("x2 + crc2: " + x2 + crc2)

	# Compute delta (xor) of x1 and x2:
	xd = hexxor(x1, x2)
	crcd = hexxor(crc1, crc2)
	print("xd: " + xd)
	print("crcd: " + crcd)

	hack_cipher = xd + crcd
	print("hack cipher: " + hack_cipher)

	result = hexxor(initial_cipher, hack_cipher)
	key = hexxor(initial_cipher, s1.encode().hex() + crc1)
	decoded_plaintext = hexxor(result, key)
	print("new text: " + bytes.fromhex(decoded_plaintext[:-4]).decode())
	print("CRC: " + decoded_plaintext[-4:])

if __name__ == "__main__":
	main()
