def _otp(cipher, key):
	return ''.join([chr(ord(c) ^ key) for c in cipher])


def main():
	with open('otp.txt') as f:
		cipher = f.read()

	for k in range(256):
		plain = _otp(cipher, k)
		if plain.isprintable():
			print(plain)


if __name__ == '__main__':
	main()
