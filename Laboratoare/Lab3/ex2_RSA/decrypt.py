from gmpy2 import invert, powmod


c = 28822365203577929536184039125870638440692316100772583657817939349051546473185
n = 70736025239265239976315088690174594021646654881626421461009089480870633400973
e = 3
# Folosind FactorDB, obtinem:
p = 238324208831434331628131715304428889871
q = 296805874594538235115008173244022912163


def main():
	phi = (p - 1) * (q - 1)
	d = invert(e, phi)

	msg_num = powmod(c, d, n)
	msg = bytearray.fromhex(hex(msg_num)[2:]).decode('ascii')
	print(f'Encrypred text is: {msg}')


if __name__ == '__main__':
	main()
