#!/usr/bin/env Python3

import sys



def test(fn):
	fReader = open(fn, "rb")
	bytes = fReader.read(16)
	print("%08X " % len(bytes), end = "  ")

	for b in bytes:
		print("%02X " % b, end = "")

	for (16 - len(bytes)):
		print("   ", end = "")

	print( "  |", end = "")
	
	for b in bytes:
		if( b > 32 and b < 127 ):
			print( chr(b), end = "" )
		else:
			print( ".", end = "")

	for (16 - len(bytes)):
		print( " ", end = "")

	print("|")


def main(fileName):
	"""print("This is a test!  :D  " + fileName)
	MOWR TESTS!!!  BWAHAHAHAHA!!!"""
	test(fileName)




if __name__ == '__main__':
	main(sys.argv[1])
