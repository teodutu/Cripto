import random
import math

NUM_TESTS = 100000
LEN_STR = 100

class WeakRNG:
	"""
	Simple class for a weak RNG
	"""
	def __init__(self, a, b):
		self.rstate = 0
		self.maxn = 255
		self.a = a
		self.b = b
		self.p = 256

	def update_state(self):
		"""
		Update state
		"""
		self.rstate = (self.a * self.rstate + self.b) % self.p

def get_random_string(n):  # generate random bit string
	bstr = bin(random.getrandbits(n)).lstrip('0b').zfill(n)
	return bstr

def monobit_test(bit_seq):
	"""
	Verifica daca secventa de biti data e random sau nu
	https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf#%5B%7B%22num%22%3A141%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22Fit%22%7D%5D
	"""
	sum = 0
	for bit in bit_seq:
		if bit == '0':
			sum -= 1
		else:
			sum +=1

	return math.erfc(math.fabs(sum) / math.sqrt(20)) >= 0.01

def hex2bin(hs):
	bs = ""
	for c in hs:
		bs = bs + bin(int(c, 16))[2:].zfill(4)

	return bs

if __name__ == "__main__":
	wr = WeakRNG(7, 5)
	count_WR = 0
	count_random = 0

	for _ in range(NUM_TESTS):
		rng = b""
		for _ in range(LEN_STR):
			wr.update_state()
			rng += bytes([wr.rstate])
		count_WR += monobit_test(hex2bin(rng.hex()))

		random_str = get_random_string(LEN_STR * 8)
		count_random += monobit_test(random_str)

	probab_WR = count_WR / NUM_TESTS
	probab_random = count_random / NUM_TESTS

	print("The probabilty that the RNG's output is random is {}"
		.format(probab_WR))
	print("The probabilty that the the randomly generated bits are random is {}"
		.format(probab_random))
