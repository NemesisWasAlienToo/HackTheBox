import string

def decryption(msg):
    ct = []
    for char in msg:
        ct.append((179 * (char + (256 - 18))) % 256)
    return bytes(ct)

f = open('./msg.enc','r')
CypherText = f.read()
f.close()

CypherBytes = bytes.fromhex(CypherText)

PlainByes = decryption(CypherBytes)

# PlainText = PlainByes.decode()

# print(PlainText)

print(PlainByes)