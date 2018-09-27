import math
import random
import csv

class Inflammation: 

	def __init__(self, temp, nausea, lumb_p, urine_p, mict_p, ureth_b, b_inflamed):
		self.attr = []
		self.temp = temp
		self.nausea = nausea
		self.lumb_p = lumb_p
		self.urine_p = urine_p
		self.mict_p = mict_p
		self.ureth_b = ureth_b
		self.b_inflamed = b_inflamed

		self.attr.append(temp)
		self.attr.append(nausea)
		self.attr.append(lumb_p)
		self.attr.append(urine_p)
		self.attr.append(mict_p)
		self.attr.append(ureth_b)
		self.attr.append(b_inflamed)

	def guess_class(self, p, weights):
		num = 0
		for i in range(5):
			num += weights[i] * p[i]
		num += weights[5]
		if num > 0:
			return 1
		else:
			return 0

	def adjust_weights(self, p, w, learn_rate, outcome):
		weights = w
		if(p[5] != outcome):
			for i in range(len(weights) - 1):
				weights[i] = weights[i] + (learn_rate * (p[5] - outcome))*p[i]
			weights[5] = weights[5] + (learn_rate * (p[5] - outcome))
		return weights

	def epoch(self, epochs, dataset, weights, learn_rate):
		with open('results.csv', 'w', newline = '') as f:
			writer = csv.writer(f)
			while(epochs < 256):
				errors = 0
				for p in dataset:
					guess = self.guess_class(p.attr, weights)
					if guess != p.b_inflamed:
						errors += 1
					weights = self.adjust_weights(p.attr, weights, learn_rate, guess) 
				epochs += 1 
				random.shuffle(dataset)
				valtuple = ((errors/len(dataset) * 100), epochs)
				writer.writerow(valtuple)
				print("error rate: ", str(errors/len(dataset) * 100) + "\n" + str(weights) + str(epochs))

		return weights

	def test(self, dataset, learn_rate, weights):
		weights = []
		for x in range(6):
			weights.append(1)#random.uniform(0, 1) is random numbers vs just 1s significant? 
		weights = self.epoch(0, dataset, weights, learn_rate)
		return weights 
		

def loaddata():
	with open('diagnosis.txt', encoding="utf8", errors='ignore') as f: 
		list = []
		dataset = []
		y = 0
		for line in f:
			list.append(line)
		for x in range(len(list)):
			line = list[x].split()

			for y in range(len(line)): 
				line[y] = line[y].replace('\n', '').replace('\x00', '')
				if line[y] == 'no':
					line[y] = 0
				elif line[y] == 'yes':
					line[y] = 1	
				y = y+1
			y = 0
			if(line[0] != ''):
				temp = float(line[0].replace('\x00', '').replace(',', '.')) 
				temp = (temp - 35.5) / (41.5 - 35.5)
				nausea = line[1]
				lumb_p = line[2]
				urine_p = line[3]
				mict_p = line[4]
				ureth_b = line[5]
				b_inflamed = line[6]
				i = Inflammation(temp, nausea, lumb_p, urine_p, mict_p, ureth_b, b_inflamed)
			x = x + 1
			dataset.append(i)
		return dataset
	
dataset = loaddata() #dataset
testset = []
training = [] 
learn_rate = 0.5

for x in range(len(dataset)):
	if x < 30:
		testset.append(dataset[x])
	else: 
		training.append(dataset[x])
x = x + 1

i = Inflammation(testset[0].temp, testset[0].nausea, testset[0].lumb_p, 
		  	testset[0].urine_p, testset[0].mict_p, testset[0].ureth_b, 
		  	testset[0].b_inflamed)

trainedwts = i.test(dataset, 0.5, [])
print("training set:", str(trainedwts))
finalwts = i.test(testset, 0.5, trainedwts)
print("test set:", str(finalwts))

