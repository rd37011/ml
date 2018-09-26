import math
import pickle

class Inflammation: 

	def __init__(self, temp, nausea, lumb_p, urine_p, mict_p, ureth_b, b_inflamed, nephr_ipo):
		self.attr = []
		self.temp = temp
		self.nausea = nausea
		self.lumb_p = lumb_p
		self.urine_p = urine_p
		self.mict_p = mict_p
		self.ureth_b = ureth_b
		self.b_inflamed = b_inflamed
		self.nephr_ipo = nephr_ipo

		self.attr.append(temp)
		self.attr.append(nausea)
		self.attr.append(lumb_p)
		self.attr.append(urine_p)
		self.attr.append(mict_p)
		self.attr.append(ureth_b)
		self.attr.append(b_inflamed)
		self.attr.append(nephr_ipo)

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
				#print(line[y])
				y = y+1
			#print(line)
			y = 0
			if(line[0] != ''):
				temp = float(line[0].replace('\x00', '').replace(',', '.'))# need float
				nausea = line[1]
				lumb_p = line[2]
				urine_p = line[3]
				mict_p = line[4]
				ureth_b = line[5]
				b_inflamed = line[6]
				nephr_ipo = line[7]
				i = Inflammation(temp, nausea, lumb_p, urine_p, mict_p, ureth_b, b_inflamed, nephr_ipo)
			x = x + 1
			dataset.append(i)
		return dataset
	
trainingset = loaddata() #dataset
for x in range(len(trainingset)):
	print(trainingset[x].temp, trainingset[x].nausea, trainingset[x].lumb_p, 
		  trainingset[x].urine_p, trainingset[x].mict_p, trainingset[x].ureth_b, 
		  trainingset[x].b_inflamed,trainingset[x].nephr_ipo)
	x = x + 1