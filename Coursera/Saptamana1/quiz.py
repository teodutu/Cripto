plain1 = b"attack at dawn"
plain2 = b"attack at dusk"
cipher1 = b"\x09\xe1\xc5\xf7\x0a\x65\xac\x51\x94\x58\xe7\xe5\x3f\x36"

cipher2 = b""
for i in range(len(plain1)):
    cipher2 += bytes([plain1[i] ^ cipher1[i] ^ plain2[i]])

print(bytearray(cipher2).hex())