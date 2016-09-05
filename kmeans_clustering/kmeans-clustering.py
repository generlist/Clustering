import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

def distance(centroid, sample):
	return sqrt(pow(centroid[0] - sample[0], 2) + pow(centroid[1] - sample[1], 2))

def process_input(line):
	x, y = line.split(",")
	samples.append((float(x.strip()), float(y.strip())))

def categorizeIntoClusters():
	global centroids
	global clusters
	counter = 0
	while counter < 100:
		counter += 1
		for sample in samples:
			minDist = 1000000000.0 
			ind = -1
			for i in range(len(centroids)):
				if minDist > distance(centroids[i], sample):
					minDist = distance(centroids[i], sample)
					ind = i
			clusters[ind].append(sample)
		newCentroids = []
		for i in range(len(centroids)):
			try:
				newx = sum([x for x,y in clusters[i]]) / len(clusters[i])
				newy = sum([y for x,y in clusters[i]]) / len(clusters[i])
				newCentroids.append((newx, newy))
			except Exception, e:
				newCentroids.append(centroids[i])
		raw_input("ENTER for next step >> ")
		plt.gcf().clear()
		for i in range(len(centroids)):
			xlist = newCentroids[i][0]
			ylist = newCentroids[i][1]
			xlist2 = [x for x,y in clusters[i]]
			ylist2 = [y for x,y in clusters[i]]
			plt.scatter(xlist2, ylist2, s=100, color=colors[i])
			plt.scatter(xlist, ylist, s=100, marker='^', color=colors[i], edgecolor="black")
			
		clusters = {}
		centroids = []
		for i in range(len(newCentroids)):
			clusters[i] = []
		centroids = [(x,y) for x,y in newCentroids]


samples = []
centroids = []
colors = []

# input
fname = raw_input("Input file: ")
content = []
with open(fname) as f:
    content = f.readlines()

for line in content:
	process_input(line)

maxx = max([x for x,y in samples])
maxy = max([y for x,y in samples])
minx = min([x for x,y in samples])
miny = min([y for x,y in samples])

numOfClusters = int(raw_input("Number of clusters: "))
clusters = {}

for i in range(numOfClusters):
	#random initialization of starting centroids
	centroids.append((np.random.uniform(minx-1, maxx+1), np.random.uniform(miny-1, maxy+1)))
	clusters[i] = []
	colors.append(np.random.rand(3,1))

plt.ion()
plt.pause(0.1)
plt.gcf().clear()
xlist2 = [x for x,y in samples]
ylist2 = [y for x,y in samples]
plt.scatter(xlist2, ylist2, s=100)
for i in range(len(centroids)):
	xlist = centroids[i][0]
	ylist = centroids[i][1]
	plt.scatter(xlist, ylist, s=100, marker='^', color=colors[i], edgecolor="black")

categorizeIntoClusters()