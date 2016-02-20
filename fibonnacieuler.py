#!/usr/bin/env python3

def main():
	a,b = 1,2
	sum = 0;
	
	while a<= 4000000:
		a,b=b,a+b
		print(a)
		if a%2==0:
			sum+=a
	
	print (sum)
	
main()
	
