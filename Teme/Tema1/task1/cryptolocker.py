#!/usr/bin/env python3

import sys
import binascii


def keystream(key, length):
	result = bytearray()
	for i in range(length):
		k = 67
		if len(result) < len(key):
			k = k ^ key[i]
		else:
			k = result[i - len(key)] ^ key[i % len(key)]
		result.append(k)
	return result


def encrypt(data, key):
	return bytes([(data[idx] ^ k) for idx, k in enumerate(keystream(key, len(data)))])


def xor_data(data1, data2):
	return bytes([(data1[i] ^ data2[i]) for i in range(len(data1))])


def try_string(xored, s):
	print(f'Trying string {s}:\n===============================================\n')
	for i in range(len(s)):
		key = b'a' * i + s * 600
		print(
			xor_data(xored, key).decode('ascii', errors='ignore'),
			end='\n\n===============================================\n\n'
		)
		# input()


if __name__ == "__main__":
	chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 \n.,!?'
	# the = b'https://www.youtube.com/watch' * 300
	# The = b'a' + b'me s' * 300

	with open('flrns.txt.bin', "rb") as f:
		data_flrns = f.read()
	with open('plmb.txt.bin', "rb") as f:
		data_plmb = f.read()
	
	xored = xor_data(data_flrns, data_plmb)
	line = ''

	for c in xored.decode('ascii', errors='ignore'):
		if c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z':
			line += c
		else:
			line += '-'
	print(line)

	# try_string(xored, b'https://www.youtube.com/watch')
	try_string(xored, b' decr')
	# try_string(xored, b'SpeishFlag')
	# try_string(xored, b'flag')
	# try_string(xored, b'Eu mereu Eu')
	# try_string(xored, b'binary')

	# print(xor_data(xored, the).decode('ascii', errors='ignore'))
	# print('\nasdf\n')
	# interesting = xor_data(xored, The)
	# print(xor_data(xored, The))

	# if len(sys.argv) < 4:
	#     print("Usage: cryptolocker.py <SOURCE_FILE> <DESTINATION_FILE> <KEY>")
	#     sys.exit(2)

	# if len(sys.argv[3]) < 7:
	#     print("Key is too short!")
	#     sys.exit(2)
	# if len(sys.argv[3]) > 11:
	#     print("Key is too long!")
	#     sys.exit(2)

	# # read the input file
	# in_data = None
	# with open(sys.argv[1], "rb") as f:
	#     in_data = f.read()

	# # encode the key in binary
	# key = sys.argv[3].encode('ascii', errors='ignore')
	# # encrypt the file
	# out_data = encrypt(in_data, key)
	# # save the encrypted file
	# with open(sys.argv[2], "wb") as f:
	#     f.write(out_data)

