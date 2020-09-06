import sys
import random
import string
from operator import itemgetter
import time
import bisect
from Crypto.Cipher import DES

def strxor(a, b): # xor two strings (trims the longer input)
	return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])


def hexxor(a, b): # xor two hex strings (trims the longer input)
	ha = a.decode('hex')
	hb = b.decode('hex')
	return "".join([chr(ord(x) ^ ord(y)).encode('hex') for (x, y) in zip(ha, hb)])


def bitxor(a, b): # xor two bit strings (trims the longer input)
	return "".join([str(int(x)^int(y)) for (x, y) in zip(a, b)])


def str2bin(ss):
	"""
	Transform a string (e.g. 'Hello') into a string of bits
	"""
	bs = ''
	for c in ss:
		bs = bs + bin(ord(c))[2:].zfill(8)
	return bs


def str2int(ss):
	"""
	Transform a string (e.g. 'Hello') into a (long) integer by converting first
	to a bistream
	"""
	bs = str2bin(ss)
	li = int(bs, 2)
	return li


def hex2bin(hs):
	"""
	Transform a hex string (e.g. 'a2') into a string of bits (e.g.10100010)
	"""
	bs = ''
	for c in hs:
		bs = bs + bin(int(c,16))[2:].zfill(4)
	return bs


def bin2hex(bs):
	"""
	Transform a bit string into a hex string
	"""
	bv = int(bs,2)
	return int2hexstring(bv)


def byte2bin(bval):
	"""
	Transform a byte (8-bit) value into a bitstring
	"""
	return bin(bval)[2:].zfill(8)


def int2hexstring(bval):
	"""
	Transform an int value into a hexstring (even number of characters)
	"""
	hs = hex(bval)[2:]
	lh = len(hs)
	return hs.zfill(lh + lh%2)


def get_index(a, x):
	"""
	Locate the leftmost value exactly equal to x in list a
	"""
	i = bisect.bisect_left(a, x)
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

	# TODO: implement des2_enc and des2_dec
	m1 = des2_dec(key1, key2, bytes.fromhex(c1))
	print("plaintext1: " + m1.decode("ascii"))

	c2 = "54826ea0937a2c34d47f4595f3844445520c0995331e5d492f55abcf9d8dfadf"
	m2 = des2_dec(key1, key2, bytes.fromhex(c2))
	print("plaintext2: " + m2.decode("ascii"))

	m12 = des2_dec(key1, key2, bytes.fromhex(c1 + c2))
	print("plaintext1 + 2: " + m12.decode("ascii"))

	# TODO: run meet-in-the-middle attack for the following plaintext/ciphertext
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
