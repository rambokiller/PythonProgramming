#!/usr/bin/env python3
# A simple program illustrating a chaotic function

def main():
	print("This program illustrates a chaotic function")
	x = eval(input("Enter a number between 0 and 1:"))
	n = eval(input("How many numbers should I print?"))
	for i in range(n):
		x = 2.0 * x * (1-x)
		print(x)

main()
"""
print("Hello, world!")
print("Hello", "world!")
print(3)
print(3.0)
print(2+3)
print(2.0 + 3.0)
print("2+3=",2+3)
print(2*3)
print(2**3)
print(2/3)
"""
