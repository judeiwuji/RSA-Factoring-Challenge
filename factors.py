#!/usr/bin/python3
from math import ceil, sqrt
from sys import argv, stderr, exit

def factorize(n):
	p, q = 1, n
	d = ceil(sqrt(n)) + 1
	for i in range(2, d):
		if n % i == 0:
			p, q = i, int(n / i)
			break
	return (p, q)

def main():
	if(len(argv) != 2):
		stderr.write("Usage: factors <file>\n")
		exit(1)
	with open(argv[1]) as file:
		for n in file:
			n = int(n)
			p, q = factorize(n)
			print("{:d}={:d}*{:d}".format(n, q, p))

if __name__ == "__main__":
	main()
