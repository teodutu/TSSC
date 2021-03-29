CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 \n.,!?'


def xor_data(data1, data2):
	return bytes([(data1[i] ^ data2[i])
		for i in range(min(len(data1), len(data2)))])


def xor_67(data):
	return bytes([data[i] ^ 67 for i in range(len(data))])


def print_decoded(data):
	print('\n==============================================\n')
	line = ''
	for c in data.decode('ascii', errors='ignore'):
		if c in CHARS:
			line += c
		else:
			line += '-'
	print(line)
	print('\n==============================================\n')


SALAM = b'''Am pe cineva
Vine seama in urma mea
Ala este paza mea

Noi ne respectam ca fratii
SpeishFlag'''


if __name__ == "__main__":
	with open('flrns.txt.bin', 'rb') as f:
		data_flrns = f.read()
	with open('plmb.txt.bin', 'rb') as f:
		data_plmb = f.read()
	
	xored = xor_data(data_flrns, data_plmb)
	xored_flrns_67 = xor_67(data_flrns)
	xored_plmb_67 = xor_67(data_plmb)

	print_decoded(xored_flrns_67)
	print_decoded(xored_plmb_67)

	print(xor_data(SALAM, data_flrns))
	key = b'!,*+:qq)3CCCCCCCCC' * 1000

	print_decoded(xor_data(data_flrns, key))
	print_decoded(xor_data(data_plmb, key))
