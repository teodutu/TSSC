from base64 import b64decode

with open('b64.txt') as f:
	cipher = f.read()
	num_encryptions = 0

	while cipher[:5] != b'FLAG{':
		cipher = b64decode(cipher)
		num_encryptions += 1
	
	print(f'The file was base64-encrypted {num_encryptions} times and'
		f'contained the flag: {cipher.decode("ascii")}')
