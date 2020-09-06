from operator import itemgetter
from bisect import bisect_left
from Crypto.Cipher import DES


def get_index(a, x):
	"""
	Locate the leftmost value exactly equal to x in list a
	"""
	i = bisect_left(a, x)
	if i != len(a) and a[i] == x:
		return i
	else:
		return -1


def des_enc(k, m):
	"""
	Encrypt a message m with a key k using DES as follows:
	c = DES(k, m)

	Args:
		m should be a bytestring (i.e. a sequence of characters such as "Hello"
			or "\x02\x04")
		k should be a bytestring of length exactly 8 bytes.

	Note that for DES the key is given as 8 bytes, where the last bit of
	each byte is just a parity bit, giving the actual key of 56 bits, as expected for DES.
	The parity bits are ignored.

	Return:
		The bytestring ciphertext c
	"""
	d = DES.new(k)
	c = d.encrypt(m)

	return c


def des_dec(k, c):
	"""
	Decrypt a message c with a key k using DES as follows:
	m = DES(k, c)

	Args:
		c should be a bytestring (i.e. a sequence of characters such as "Hello"
			or "\x02\x04")
		k should be a bytestring of length exactly 8 bytes.

	Note that for DES the key is given as 8 bytes, where the last bit of
	each byte is just a parity bit, giving the actual key of 56 bits, as expected for DES.
	The parity bits are ignored.

	Return:
		The bytestring plaintext m
	"""
	d = DES.new(k)
	m = d.decrypt(c)

	return m


def des2_dec(k1, k2, c):
	return des_dec(k2, des_dec(k1, c))


def des2_enc(k1, k2, m):
	return des_enc(k1, des_enc(k2, m))


def meet_in_the_middle(key1, key2, msg1, msg2, cipher1, cipher2):
	table = []

	for i in range(128):
		for j in range(128):
			key = chr(i) + chr(j) + key2[2:]
			table.append((key, des_enc(key, msg1)))

	table_sorted = sorted(table, key=itemgetter(1))
	encryptions = [value for _, value in table_sorted]

	for i in range(128):
		for j in range(128):
			key = chr(i) + chr(j) + key1[2:]
			msg = des_dec(key, bytes.fromhex(cipher1))

			pos = get_index(encryptions, msg)
			if pos != -1:
				proposed_key2 = table_sorted[pos][0]
				if des2_enc(key, proposed_key2, msg2).hex() == cipher2:
					return (key, proposed_key2)


def main():
	# Exercitiu pentru test des2_enc
	key1 = "Smerenie"
	key2 = "Dragoste"
	m1_given = "Fericiti cei saraci cu duhul, ca"
	c1 = "cda98e4b247612e5b088a803b4277710f106beccf3d020ffcc577ddd889e2f32"

	# Test des2_dec
	m1 = des2_dec(key1, key2, bytes.fromhex(c1))
	print("plaintext1: " + m1.decode("ascii"))

	c2 = "54826ea0937a2c34d47f4595f3844445520c0995331e5d492f55abcf9d8dfadf"
	m2 = des2_dec(key1, key2, bytes.fromhex(c2))
	print("plaintext2: " + m2.decode("ascii"))

	m12 = des2_dec(key1, key2, bytes.fromhex(c1 + c2))
	print("plaintext1 + 2: " + m12.decode("ascii"))

	# Run meet-in-the-middle attack for the following plaintext/ciphertext
	m1 = "Pocainta"
	c1 = "9f98dbd6fe5f785d" # in hex string
	m2 = "Iertarea"
	c2 = "6e266642ef3069c2"

	# Note: you only need to search for the first 2 bytes of the each key:
	k1 = "??oIkvH5"
	k2 = "??GK4EoU"

	print("Keys are: {}".format(meet_in_the_middle(k1, k2, m1, m2, c1, c2)))


if __name__ == "__main__":
	main()
