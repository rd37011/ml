#Chronic Kindey Disease File Read
import os
import inspect
import csv
import math
from random import shuffle

class ckd:
    def __init__ (self, age,bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,pcv,wc,rc,htn,dm,cad,appet,pe,ane,cl):
        self.attributes = []
        if age == "?":
            age = 0
        self.attributes.append(float(age)) #numeric
        if bp == "?":
            bp = 0
        self.attributes.append(float(bp)) #numeric
        if sg == "?":
            sg = 0
        self.attributes.append(float(sg)) #1.005 - 1.025
        if al == "?":
            al = 0
        self.attributes.append(float(al)) # 0-5
        if su == "?":
            su = 0
        self.attributes.append(float(su))# 0-5
        if rbc=="abnormal":
            rbc = 1
        elif rbc=="normal":
            rbc= 0
        else:
            rbc = float(0)
        self.attributes.append(rbc)
        if pc=="abnormal":
            pc = 1
        elif pc=="normal":
            pc= 0
        else:
            pc = float(0)
        self.attributes.append(pc)
        if pcc=="notpresent":
            pcc = 1
        elif pcc =='present':
            pcc = 0
        else:
            pcc = float(0)
        self.attributes.append(pcc)
        if ba=="notpresent":
            ba = 1
        elif ba =='present':
            ba = 0
        else:
            ba = float(0)
        self.attributes.append(ba)
        if bgr == "?":
            bgr = 0
        self.attributes.append(float(bgr)) #numeric
        if bu == "?":
            bu = 0
        self.attributes.append(float(bu))#numeric
        if sc == "?":
            sc = 0
        self.attributes.append(float(sc)) #numeric
        if sod == "?":
            sod = 0
        self.attributes.append(float(sod)) #numeric
        if pot == "?":
            pot = 0
        self.attributes.append(float(pot)) #numeric
        if hemo == "?"or hemo == "\t?":
            hemo = 0
        self.attributes.append(float(hemo)) #numeric
        if pcv == "\t?" or pcv == "?":
            pcv = 0
        self.attributes.append(float(pcv)) #numeric
        if wc == "?"or wc == "\t?":
            wc = 0
        self.attributes.append(float(wc)) #numeric
        if rc == "?" or rc == "\t?":
            rc = 0
        self.attributes.append(float(rc)) #numeric
        if htn=="no":
            htn = 1
        elif htn =='yes':
            htn = 0
        else:
            htn = float(0)
        self.attributes.append(htn)
        if dm=="no":
            dm = 1
        elif dm =='yes':
            dm = 0
        else:
            dm = float(0)
        self.attributes.append(dm)
        if cad=="no":
            cad = 1
        elif cad =='yes':
            cad = 0
        else:
            cad = float(0)
        self.attributes.append(cad)
        if appet=="poor":
            appet = 1
        elif appet =='good':
            appet = 0
        else:
            appet = float(0)
        self.attributes.append(appet)
        if pe=="no":
            pe = 1
        elif pe =='yes':
            pe = 0
        else:
            pe = float(0)
        self.attributes.append(pe)
        if ane=="no":
            ane = 1
        elif ane =='yes':
            ane = 0
        else:
            ane = float(0)
        self.attributes.append(ane)
        if cl=="ckd":
            cl = 1
        else:
            cl = 0
        self.attributes.append(cl)

    def print(self):
        print(self.attributes)

class normalizedCDK:
    def __init__ (self, attrib ,cl):
        self.attributes = attrib
        self.cl = (cl)
    
def normalize(arr):
    min = [math.inf] * 25
    max = [0] * 25
    newData = []
    for a in arr:
        for index, s in enumerate(a.attributes):
            #print(s)
            if s < min[index]:
                min[index] = s
            elif s > max[index]:
                max[index] = s
    #print(min)
    #print(max)
    temp = [] * 25
    for i, a in enumerate(arr):
        for index, s in enumerate(a.attributes):
            s = (s - min[index])/(max[index] - min[index])
            temp.append(s)
        #print(temp, "  |||||  ")
        newData.append(temp)
        temp = []
    #print(newData, " ")

    f = open("ckdData.txt", "w")
    g = open("ckdOutput.csv", "w")
    for index, val in enumerate(newData):
        for index,a in enumerate(val):
            #print(a)
            f.write(str(a))
            g.write(str(a))
            f.write(" ")
            g.write(",")
        f.write("\n")
        g.write("\n")
    f.close()
    g.close()
    return newData



file = os.getcwd()
filepath = os.path.join(file,"Chronic_Kidney_Disease")
file = os.path.join(filepath, "ckd_data.csv")
#print(file)
data = []

with open(file,"r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            datum = ckd(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23], row[24])
            #datum.print()
            data.append(datum)
            line_count += 1

#printArray(data)
def guess_class(p, weights):
    num = 0
    for i in range(len(p.attributes)):
        num += weights[i] * p.attributes[i]
    num += weights[24]
    #print("Class of P ", p.cl, " Guess Number ", num)
    if num > 0:
        if p.cl != 1.0:
            print("False Positive")
            #print(num, p.attributes, p.cl)
        #print("positive")
        return 1
    else:
        if p.cl != 0.0:
            print("False Negative")
            #print(num, p.attributes, p.cl)
        #print("negative")
        return 0


def adjust_weights(p, w, learn_rate, outcome):
    #print("Outcome", outcome, "Actual Class ", p.cl)
    weights = w
    if (p.cl != outcome):
        print("Starting Weight Vector", w)
        for i in range(len(weights) - 1):
            weights[i] = weights[i] + (learn_rate * (p.cl - outcome))*p.attributes[i]
        weights[23] = weights[23] + (learn_rate * (p.cl - outcome))
        print("Ending Weight Vector", weights)
    return weights


def epoch(parray, w, learn_rate):
    weights = w
    for p in parray:
        guess = guess_class(p, weights)
        weights = adjust_weights(p, weights, learn_rate, guess)
    
    print(weights)

def epochTest(parray, w, learn_rate):
    weights = w
    num = 0
    for p in parray:
        guess = guess_class(p, weights)
        if p.cl!=guess:
            num = num + 1
    xlFile.write(str(num) +"," + str(learn_rate) + "\n" )
    
    
    

data = normalize(data)
def normalizeCKD(data):
    normalizedData = []
    for d in data:
        c = normalizedCDK(d[:24],d[24])
        normalizedData.append(c)
    return normalizedData
normalizedData = normalizeCKD(data)

posData = normalizedData[:250]
negData = normalizedData[250:]

testSet = []

for a in posData[:50]:
    testSet.append(a)
for b in negData[:50]:
    testSet.append(b)

trainingSet = []
for a in posData[50:]:
    trainingSet.append(a)
for b in negData[50:]:
    trainingSet.append(b)

weights = [1] * 25
shuffle(trainingSet)
learn_rate = .05
xlFile = open("CKD_OUTPUT.csv", "w")
for i in range(255):
    epoch(trainingSet, weights, learn_rate)
    epochTest(testSet, weights, learn_rate)
    learn_rate = learn_rate + .05
    weights = [1] * 25

#print(trainingSet)
#print(trainingSet[299][24])