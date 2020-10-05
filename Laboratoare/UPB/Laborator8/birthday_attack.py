from hashlib import sha256
import random


MSG_LEN = 8


def main():
	# Try to find a collision on the first 4 bytes (32 bits).
	# Step 1. Generate 2^16 different random messages.
	# Step 2. Compute hashes
	# Step 3. Check if there exist two hashes that match in the first four
	# bytes.
	# Step 3a. If a match is found, print the messages and hashes.
	# Step 3b. If no match is found, repeat the attack with a new set of random
	# messages.
	num_iter = 1
	collision = False

	while not collision:
		hashes = {}

		for _ in range(2 ** 16):
			message = b"".join(bytes([random.randint(0, 255)])
				for _ in range(MSG_LEN))
			short_hash = sha256(message).digest()[:4]

			if short_hash in hashes:
				print(f"Found collision for messages '{message.hex()}' and "
					f"'{hashes[short_hash].hex()}': {short_hash.hex()} on "
					f"iteration {num_iter}.")
				collision = True
				break

			hashes[short_hash] = message

		num_iter += 1


if __name__ == "__main__":
	main()
