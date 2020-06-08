'''
A competitve programming template in Python3 
--Compiler to be used pypy3
'''

import sys 
input=sys.stdin.readline 

################ -------- Input FUcntions ----------############
def inp():
	'''
	For taking integer inputs
	'''
	return (int(input()))

def inlt():
	'''
	For taking list inputs
	'''
	return (list(map(int,input().split())))

def insr():
	'''
	Taking string inopouts.
	Returns a lsit of chars insetad of a string ,therefore 
	easier to use
	'''
	s=input()
	return (list(s[:len(s)-1]))

def invr():
	'''Takig space spe integer varibale inputs
	'''
	return(map(int,input().split()))


