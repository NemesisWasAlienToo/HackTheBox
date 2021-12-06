CHARS: bytes = [108, 82, 167, 69, 39, 234, 241, 10, 160, 76, 225, 1, 97, 114, 10, 250, 155, 101, 97, 115, 207, 190, 196, 192]
FLAGS_RAW: bytes = [182, 176, 158, 222, 102, 14, 16, 218, 108, 234, 224, 12, 122, 90, 90, 14, 80, 186, 218, 218, 76, 174, 84, 144]
FLAGS = [i ^ 0x4A for i in FLAGS_RAW]

FL_NEGATE = 1 << 1
FL_XORBY6B = 1 << 3
FL_XORBY3E = 1 << 4
FL_SWAPBYTES = 1 << 6


def CheckFlag(f, flag) -> bool:
    return ((f & flag) != 0)


def ValidateChar(char):
    if type(char) is str and len(char) == 1:
        char = ord(char[0])
    return char


def XorBy6B(char):
    char = ValidateChar(char)
    return chr(char ^ 0x6B)


def XorBy3E(char):
    char = ValidateChar(char)
    return chr(char ^ 0x3E)


def NegateChar(char):
    char = ValidateChar(char)
    return chr(255 - char)


# Decrypt


def DSwapChar(char):
    char = ValidateChar(char) ^ 0xBD

    SMALL = char & 0xf
    BIG = (char >> 4) & 0xf

    return chr((SMALL << 4) | BIG)


def DecryptCharacter(flag, char):
    if CheckFlag(flag, FL_XORBY3E):
        char = XorBy3E(char)
    if CheckFlag(flag, FL_XORBY6B):
        char = XorBy6B(char)
    if CheckFlag(flag, FL_NEGATE):
        char = NegateChar(char)
    if CheckFlag(flag, FL_SWAPBYTES):
        char = DSwapChar(char)

    return char


# Encrypt


def ESwapChar(char):
    char = ValidateChar(char)

    BIG = (char >> 4) & 0xf
    SMALL = char & 0xf

    return chr(((SMALL << 4) | BIG) ^ 0xBD)


def EncryptCharacter(flag, char):
    if CheckFlag(flag, FL_SWAPBYTES):
        char = ESwapChar(char)
    if CheckFlag(flag, FL_NEGATE):
        char = NegateChar(char)
    if CheckFlag(flag, FL_XORBY6B):
        char = XorBy6B(char)
    if CheckFlag(flag, FL_XORBY3E):
        char = XorBy3E(char)

    return char


for i in range(65, 91):
    flag = FL_SWAPBYTES
    char = chr(i)
    coded = EncryptCharacter(flag, char)
    decoded = DecryptCharacter(flag, coded)
    if (char != decoded):
        print(f"{char} : {coded} -> {decoded}")

output: str = ""

for i in range(0, len(CHARS)):
    char = CHARS[i]
    flag = FLAGS[i]
    decoded = DecryptCharacter(flag, char)
    output += str(decoded)

print(output)