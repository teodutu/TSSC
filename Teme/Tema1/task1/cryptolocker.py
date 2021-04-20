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


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: cryptolocker.py <SOURCE_FILE> <DESTINATION_FILE> <KEY>")
        sys.exit(2)

    if len(sys.argv[3]) < 7:
        print("Key is too short!")
        sys.exit(2)
    if len(sys.argv[3]) > 11:
        print("Key is too long!")
        sys.exit(2)

    # read the input file
    in_data = None
    with open(sys.argv[1], "rb") as f:
        in_data = f.read()

    # encode the key in binary
    key = sys.argv[3].encode('ascii', errors='ignore')
    # encrypt the file
    out_data = encrypt(in_data, key)
    # save the encrypted file
    with open(sys.argv[2], "wb") as f:
        f.write(out_data)

