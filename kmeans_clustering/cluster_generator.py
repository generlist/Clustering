import numpy as np

numOfClusters = int(raw_input("Number of cluster to generate: "))
noisePoints = int(raw_input("Noise (random generated points): "))
pointsInCluster = int(raw_input("Number of points per cluster: "))
fname = raw_input("Output file name: ")
miny = -100
maxy = 100
minx = -100
maxx = 100
rangeOfCluster = 30
lines = []
for i in range(numOfClusters):
	centerX = np.random.uniform(minx, maxx)
	centerY = np.random.uniform(miny, maxy)
	for j in range(pointsInCluster):
		x = np.random.uniform(centerX - rangeOfCluster, centerX + rangeOfCluster)
		y = np.random.uniform(centerY - rangeOfCluster, centerY + rangeOfCluster)
		lines.append(str(x) + "," + str(y)+"\n")
for j in range(noisePointsPerCluster):
	lines.append(str(np.random.uniform(minx, maxx)) + "," + str(np.random.uniform(miny, maxy)) + "\n")
f = open(fname,'w')
f.writelines(lines)
f.close()
