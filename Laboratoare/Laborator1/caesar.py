import sys
import random
import string
import operator

alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar_enc(letter, k = 3):
	if letter < 'A' or letter > 'Z':
		print('Invalid letter')
		return
	else:
		return alphabet[(ord(letter) - ord('A') + k) % len(alphabet)]

def caesar_enc_string(plaintext, k = 3):
	ciphertext = ''
	for letter in plaintext:
		ciphertext = ciphertext + caesar_enc(letter, k)
	return ciphertext

def caesar_dec(letter, k = 3):
	if letter < 'A' or letter > 'Z':
		print('Invalid letter')
		return
	else:
		return alphabet[(ord(letter) - ord('A') - k) % len(alphabet)]

def caesar_dec_string(cyphertext, k = 3):
	return "".join(["" + caesar_dec(c, k) for c in cyphertext])

def main():
	m = 'BINEATIVENIT'
	k = 10

	c = caesar_enc_string(m, k)
	print(c)
	m = caesar_dec_string(c, k)
	print(m)

if __name__ == "__main__":
	main()
