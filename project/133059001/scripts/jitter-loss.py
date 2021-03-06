#! /usr/bin/python3

import sys
import math
import csv

def avg(X):
	n = len(X)
	if n > 0:
		return math.fsum(X) / len(X)
	else:
		return 0

def variance(X):
	X2 = [x**2 for x in X]
	return avg(X2) - (avg(X)**2)

def std_dev(X):
	return math.sqrt(variance(X))

with open(sys.argv[1]) as file:
	reader = csv.reader(file)
	data = [[float(row[0]), int(float(row[1])), float(row[2]), float(row[3])] for row in reader]
	hops = set([row[1] for row in data])
	error = set([row[0] for row in data])

	hop = 3
	#print("\"No. of hops =", hop, "\"")
	for err in error:
		print("\"Link Error Rate =", err, "\"")
		jitter_loss = [row[2:] for row in data if (row[0] == err) and (row[1] == hop)]
		for row in jitter_loss:
			print(row[0], row[1])
		print('\n')

		
	
		
	

