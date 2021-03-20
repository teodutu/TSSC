import subprocess as sub


ORIGINAL_MSG = b'FIRE_NUKES_MELA!'
MODIFIED_MSG = b'SEND_NUDES_MELA!'
IV = '7ec00bc6fd663984c1b6c6fd95ceeef1'


def _get_new_iv():
	iv = bytes.fromhex(IV)
	return b''.join([bytes(
		[iv[i] ^ ORIGINAL_MSG[i] ^ MODIFIED_MSG[i]
			for i in range(len(iv))]
	)])


def main():
	new_iv = _get_new_iv().hex()
	proc = sub.Popen(['./oracle', new_iv])


if __name__ == '__main__':
	main()
