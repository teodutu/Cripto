import sys
import random
import string
import operator

# Parameters for weak LC RNG
class WeakRNG:
	"""
	Simple class for a weak RNG
	"""
	def __init__(self):
		self.rstate = 0
		self.maxn = 255
		self.a = 0 # Set this to correct value
		self.b = 0 # Set this to correct value
		self.p = 257

	def update_state(self):
		"""
		Update state
		"""
		self.rstate = (self.a * self.rstate + self.b) % self.p

def strxor(a, b): # xor two strings (trims the longer input)
	return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])

def hexxor(a, b):  # xor two hex strings (trims the longer input)
	ha = bytes.fromhex(a)
	hb = bytes.fromhex(b)
	return "".join(["{:02x}".format(x ^ y) for (x, y) in zip(ha, hb)])

def main():
	# Initialise weak rng
	wr = WeakRNG()

	# Print ciphertext
	CH = "a432109f58ff6a0f2e6cb280526708baece6680acc1f5fcdb9523129434ae9f6ae9edc2f224b73a8"
	print("Full ciphertext in hex: " + CH)

	# Print known plaintext
	pknown = "Let all creation"
	nb = len(pknown)
	print("Known plaintext: " + pknown)
	pkh = pknown.encode().hex()
	print("Plaintext in hex: " + pkh)

	# Obtain first nb bytes of RNG
	gh = hexxor(pkh, CH[0:nb*2])
	print("The first {} bytes of RNG are: {}".format(nb, gh))
	gbytes = bytes.fromhex(gh)
	print("Bytes of RNG: {}".format(gbytes))

	# Break the LCG here:
	# 1. find a and b
	# 2. predict/generate rest of RNG bytes
	# 3. decrypt plaintext
	for a in range(257):
		for b in range(257):
			correct_params = True

			for i in range(1, 16):
				if gbytes[i] != (a * gbytes[i - 1] + b) % wr.p:
					correct_params = False
					break

			if correct_params:
				wr.a = a
				wr.b = b
				break

	print("Found wr.a = {}; wr.b = {}".format(wr.a, wr.b))

	# Print full plaintext
	p = "Let all creation"
	wr.rstate = gbytes[15]

	for i in range(16, len(CH) // 2):
		wr.update_state()
		p += chr(int(CH[2*i : 2*i + 2], 16) ^ wr.rstate)

	print("Full plaintext is: " + p)

if __name__ == "__main__":
	main()
