import caesar

# this is the list of bigrams, from most frequent to less frequent
bigrams = ["TH", "HE", 'IN', 'OR', 'HA', 'ET', 'AN', 'EA', 'IS', 'OU', 'HI', 'ER', 'ST', 'RE', 'ND']

# this is the list of monograms, from most frequent to less frequent
monograms = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'D', 'L', 'U', 'C', 'M', 'F', 'Y', 'W', 'G', 'P', 'B', 'V', 'K', 'X', 'Q', 'J', 'Z']

# this is the dictionary containing the substitution table (e.g. subst_table['A'] = 'B')
subst_table = {}

# these are the dictionaries containing the frequency of the mono/bigrams in the text
freq_table_bi = {}
freq_table_mono = {}

# sorts a dictionary d by the value
def sort_dictionary(d):
	sorted_dict = list(reversed(sorted(d.items(),
		key=caesar.operator.itemgetter(1))))
	return sorted_dict

# computes the frequencies of the monograms and bigrams in the text
def analize(text):
	size = len(text) - 1

	for i in range(size):
		freq_table_mono[text[i]] = freq_table_mono.get(text[i], 0) + 1
		freq_table_bi[text[i:i+2]] = freq_table_bi.get(text[i:i+2], 0) + 1

# creates a substitution table using the frequencies of the bigrams
def create_subst_table():
	freq_table_bi_sorted = sort_dictionary(freq_table_bi)

	i = 0
	size = len(bigrams)

	for bigram in freq_table_bi_sorted:
		if i >= size:
			break

		subst_table[bigram[0][0]] = bigrams[i][0]
		subst_table[bigram[0][1]] = bigrams[i][1]
		i += 1

# fills in the letters missing from the substitution table using the
# frequencies of the monograms
def complete_subst_table():
	freq_table_mono_sorted = sort_dictionary(freq_table_mono)

	i = 0
	for mono in freq_table_mono_sorted:
		if mono[0] not in subst_table:
			subst_table[mono[0]] = monograms[i]

		i += 1

# this is magic stuff used in main
def adjust():
	subst_table['Y'] = 'B'
	subst_table['E'] = 'L'
	subst_table['L'] = 'M'
	subst_table['P'] = 'W'
	subst_table['F'] = 'C'
	subst_table['X'] = 'F'
	subst_table['J'] = 'G'
	subst_table['I'] = 'Y'

def decrypt_text(ciphertext):
	plaintext = ""

	for c in ciphertext:
		if c in subst_table:
			plaintext += subst_table[c]

	return plaintext

def main():
	with open('msg_ex2.txt', 'r') as myfile:
		text = myfile.read()

	analize(text)
	create_subst_table()
	complete_subst_table()
	adjust()
	print(decrypt_text(text))

if __name__ == "__main__":
  main()
