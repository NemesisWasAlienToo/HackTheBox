import math
from random import randint, seed
from time import time, process_time


FL_NEGATE    = 1 << 1
FL_XORBY6B   = 1 << 3
FL_XORBY3E   = 1 << 4
FL_SWAPBYTES = 1 << 6


# wait for a second

currtime = int(time())
while True:
	if int(time()) - currtime != 0:
		break

# Seed random number generator

seed(int(time()) + process_time() * 1000)

def GenerateFlag():
	finalflag = 0
	if randint(0, 1) == 1:
		finalflag = finalflag | FL_SWAPBYTES
	if randint(0, 1) == 1:
		finalflag = finalflag | FL_NEGATE
	if randint(0, 1) == 1:
		finalflag = finalflag | FL_XORBY6B
	if randint(0, 1) == 1:
		finalflag = finalflag | FL_XORBY3E

	return finalflag

def CheckFlag(f, flag):
	return ((f & flag) != 0)

def ESwapChar(char : chr):
	THIS_MSB = (char >> 4) & 0xf
	THIS_LSB = char & 0xf

	return chr((THIS_MSB | (THIS_LSB << 4)) ^ 0xBD)

def XorBy6B(char : chr):
	return chr(char ^ 0x6B)

def XorBy3E(char : chr):
	return chr(char ^ 0x3E)

def NegateChar(char : chr):
	return chr(255 - char)

FLAGS = []
CHARS = []

def EncryptCharacter(char: chr):
	flag = GenerateFlag()

	if CheckFlag(flag, FL_SWAPBYTES):
		char = ESwapChar(char)
	if CheckFlag(flag, FL_NEGATE):
		char = NegateChar(char)
	if CheckFlag(flag, FL_XORBY6B):
		char = XorBy6B(char)
	if CheckFlag(flag, FL_XORBY3E):
		char = XorBy3E(char)

	return char, flag

def _Encrypt(string : str):
	for i in range(0, len(string)):
		char, flag = EncryptCharacter(string[i])

		if type(char) is int:
			char = chr(char)

		CHARS.append(char)
		FLAGS.append(chr(flag ^ 0x4A))

def Encrypt(string : str):
	_Encrypt(string)

	output = [f"{str(ord(v))} {str(ord(FLAGS[i]))}" for i, v in enumerate(CHARS)]
	file = open("output1.txt", "w")
	file.write(' '.join(output))
	file.close()
