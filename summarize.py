import collections, math, statistics

dataset = collections.OrderedDict()

with open("summary-width-cleaned.txt") as f:
	for line in f:
		data = line.strip().split(";")
		histone = str(data[0])
		mean = float(data[1])
		stdev = float(data[2])
		n = int(data[3])
		if histone not in dataset:
			dataset[histone] = [0.0, 0.0, 0.0, 0] 
			dataset[histone][0] = float(mean * n)
			dataset[histone][2] = int(n)
		else:
			dataset[histone][0] += float(mean * n)
			dataset[histone][2] += int(n)

output = open("summary-width-mean.txt", 'w')

for histone in dataset:
	dataset[histone][0] = dataset[histone][0] / dataset[histone][2]
	print("Histone: %s, Mean width: %f" % (histone, dataset[histone][0]))
	output.write("{};{}\n".format(histone, dataset[histone][0]))
