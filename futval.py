#!/usr/bin/env python3
# A program to compute the value of an investment carried
# 10 years into the future

def main():
	print("This program calculates the future value", end=" ")
	print("of a 20-year investment.")
	
	principal =eval(input("Enter the initial principal: "))
	apr = eval(input("Enter the annual interest rate: "))/100
	
	for i in range(10):
		principal = principal * (1 + apr)
		
	print("The value in 10 years is:", principal)

main()
