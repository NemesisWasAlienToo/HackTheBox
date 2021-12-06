#!/usr/bin/python3

key = []

flag = bytes.fromhex("134af6e1")
known = "HTB{".encode()

for index in range(4):
    key.append(flag[index] ^ known[index])

for item in key:
    print(hex(item))

# print(key)