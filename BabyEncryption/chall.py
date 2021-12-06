import string

def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)

ct = encryption("AAAA".encode())
f = open('./msg1.enc','w')
f.write(ct.hex())
f.close()


