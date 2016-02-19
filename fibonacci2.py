#!/usr/bin/env python3
#Program that simulates Fibonacci sequence 
#Looping Technique Method
n=eval(input("Enter term: "))

doublePrev= 0
prev = 1
nth = 1

if n==0:
	print (doublePrev)
elif n==1:
	print (prev)
else:
	while(n>nth):
		prev, doublePrev = doublePrev + prev, prev
		n=n-1
	print (prev)

	

