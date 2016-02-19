#!/usr/bin/env python3
#Program that simulates Fibonacci sequence 
#Recursion Technique Method

def fib(n):
		if n<=1:
			return 1
		return fib(n-1)+fib(n-2)

n = eval(input("What term: "))
print(fib(n))
