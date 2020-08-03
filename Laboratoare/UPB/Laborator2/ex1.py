import caesar

ciphertexts = [
	"LDPWKHORUGBRXUJRG",
	"XNTRGZKKGZUDMNNSGDQFNCRADENQDLD",
	"DTZXMFQQSTYRFPJDTZWXJQKFSDLWFAJSNRFLJ",
	"SIOMBUFFHINNUEYNBYHUGYIZNBYFILXSIOLAIXCHPUCH",
	"ERZRZOREGURFNOONGUQNLGBXRRCVGUBYL",
	"CJIJPMTJPMAVOCZMVIYTJPMHJOCZM",
	"DTZXMFQQSTYRZWIJW",
	"ZPVTIBMMOPUDPNNJUBEVMUFSZ",
	"FVBZOHSSUVAZALHS",
	"KAGETMXXZAFSUHQRMXEQFQEFUYAZKMSMUZEFKAGDZQUSTNAGD",
	"MCIGVOZZBCHRSGWFSOBMHVWBUHVOHPSZCBUGHCMCIFBSWUVPCIF"
]

def decrypt(ciphertext, searched_text):
	"""
	Decriptieaza un cifru care contine o anumita secventa de 3 caractere.

	Parameters:
		ciphertext(str): Textul criptat.
		searched_text(str): Secventa de 3 caractere care se cauta in
			`ciphertext`.

	Returns:
		Textul descifrat daca s-a gasit `searched_text` in `ciphertext`, sau
		un string gol in caz contrar.
	"""
	key = 0
	dif1 = ord(searched_text[0]) - ord(searched_text[1])
	dif2 = ord(searched_text[0]) - ord(searched_text[2])

	# 
	for i in range(len(ciphertext) - 2):
		if (
			(ord(ciphertext[i]) - ord(ciphertext[i + 1]) == dif1
			or ord(ciphertext[i + 1]) - ord(ciphertext[i]) == 26 - dif1)
			and (ord(ciphertext[i]) - ord(ciphertext[i + 2]) == dif2
			or ord(ciphertext[i + 2]) - ord(ciphertext[i]) == 26 - dif2)
		):
			key = ord(ciphertext[i]) - ord(searched_text[0])
			break

	if key == 0:
		return ""

	return caesar.caesar_dec_string(ciphertext, key)

def main():
	for c in ciphertexts:
		plaintext = decrypt(c, 'YOU')
		if plaintext == "":
			print(decrypt(c, 'THE'))
		else:
			print(plaintext)


if __name__ == "__main__":
	main()
