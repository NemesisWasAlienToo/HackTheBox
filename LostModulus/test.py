#!/usr/bin/python3
from Crypto.Util.number import getPrime, long_to_bytes, inverse
flag = "ff".encode()

class RSA:
    def __init__(self):
        self.p = getPrime(512)
        self.q = getPrime(512)
        self.e = 3 # 0x100007
        self.n = self.p * self.q
        # print(f"{hex(self.p)} * {hex(self.q)} = {hex(self.n)}")
        self.d = inverse(self.e, (self.p - 1) * (self.q - 1))
    def encrypt(self, data: bytes) -> bytes:
        pt = int(data.hex(), 16)
        ct = pow(pt, self.e, self.n)
        return long_to_bytes(ct)
    def decrypt(self, data: bytes) -> bytes:
        ct = int(data.hex(), 16)
        pt = pow(ct, self.d, self.n)
        return long_to_bytes(pt)

def main():
    print(int("ff", 16))
    print(flag.hex())
    print(flag)

    crypto = RSA()
    print ('Flag:', crypto.encrypt(flag).hex())

if __name__ == '__main__':
    main()
