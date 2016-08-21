import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from math import sqrt

def euclideanDistance(x1, x2):
	suma = 0
	for i in range(len(x1)):
		suma += pow(x1[i] - x2[i], 2)
	return sqrt(suma)

def process_input(line):
	x, y = line.split(",")
	samples.append((float(x.strip()), float(y.strip())))

def sumRow(matrix, i):
	return np.sum(matrix[i,:])

def buildSimilarityMatrix():
	numOfSamples = len(samples)
	matrix = np.zeros(shape=(numOfSamples, numOfSamples))
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			dist = euclideanDistance(samples[i], samples[j])
			if dist < threshold:
				matrix[i,j] = 1
	return matrix

def determineRow(matrix):
	maxNumOfOnes = -1
	row = -1
	for i in range(len(matrix)):
		if maxNumOfOnes < sumRow(matrix, i):
			maxNumOfOnes = sumRow(matrix, i)
			row = i
	return row

def categorizeIntoClusters(matrix):
	groups = []
	while np.sum(matrix) > 0:
		group = []
		row = determineRow(matrix)
		indexes = addIntoGroup(matrix, row)
		groups.append(indexes)
		matrix = deleteChosenRowsAndCols(matrix, indexes)
	return groups

def addIntoGroup(matrix, ind):
	change = True
	indexes = []
	for col in range(len(matrix)):
		if matrix[ind, col] == 1:
			indexes.append(col)
	while change == True:
		change = False
		numIndexes = len(indexes)
		for i in indexes:
			for col in range(len(matrix)):
				if matrix[i, col] == 1:
					if col not in indexes:
						indexes.append(col)
		numIndexes2 = len(indexes)
		if numIndexes != numIndexes2:
			change = True
	return indexes

def deleteChosenRowsAndCols(matrix, indexes):
	for i in indexes:
		matrix[i,:] = 0
		matrix[:,i] = 0
	return matrix


samples = []

# input
x1 = raw_input("Prva znacajka: ")
x2 = raw_input("Druga znacajka: ")
while True:
	line = raw_input()
	if line == "END":
		break
	process_input(line)

for x in samples:
	plt.scatter(x[0],x[1], s=100)
plt.grid()
plt.show()


threshold = int(raw_input("Threshold: "))

# build a matrix of similarity
mat = buildSimilarityMatrix()
groups = categorizeIntoClusters(mat)

#visualization
#fig = plt.figure(figsize=(10,10))
#ax = fig.add_subplot(111)
#ax.set_xlabel(x1)
#ax.set_ylabel(x2)

patches = []
for i in range(len(groups)):
	col = np.random.rand(3,1)
	patches.append(mpatches.Patch(color=col, label="Group {}".format(i+1)))
	for el in groups[i]:
		plt.scatter(samples[el][0], samples[el][1], c=col, s=100)
	#print "Grupa {}: {}".format(i+1, sorted(groups[i]))

plt.legend(handles=patches)
plt.grid()
plt.show()