import binascii

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
	return hex(int(bs,2))[2:-1]

def byte2bin(bval):
	"""
	Transform a byte (8-bit) value into a bitstring
	"""
	return bin(bval)[2:].zfill(8)
 
def str2int(ss):
	"""
	Transform a string (e.g. 'Hello') into a (long) integer by converting
	first to a bistream
	"""
	bs = str2bin(ss)
	li = int(bs, 2)
	return li

def int2hexstring(bval):
	"""
	Transform an int value into a hexstring (even number of characters)
	"""
	hs = hex(bval)[2:]
	lh = len(hs)
	return hs.zfill(lh + lh%2)

def bin2str(bs):
	"""
	Transform a binary srting into an ASCII string
	"""
	n = int(bs, 2)
	return binascii.unhexlify('%x' % n)
