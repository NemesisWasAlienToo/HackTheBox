#!/usr/bin/python3
import os
flag = open('output.txt', 'r').read().strip("Flag :")

cypher = bytes.fromhex(flag)

class XOR:
    def __init__(self):
        self.key = [0x5b, 0x1e, 0xb4, 0x9a]
    def encrypt(self, data: bytes) -> bytes:
        xored = b''
        for i in range(len(data)):
            xored += bytes([data[i] ^ self.key[i % len(self.key)]])
        return xored
    def decrypt(self, data: bytes) -> bytes:
        return self.encrypt(data)

def main():
    global flag
    crypto = XOR()
    print (crypto.encrypt(cypher))

if __name__ == '__main__':
    main()
