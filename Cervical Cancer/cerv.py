import math


class Person:

    def __init__(self, age, sexp, num_pregnancies, smokes, ysmokes, packsperyear, hcon, hcon_years, iud,
                 iud_years, std, std_num, condy, cerv_condy, vag_condy, vulvo_condy, syphilis, pelv, herp, molluscum,
                 aids, hiv, hep_b, hpv, time_first, time_last, cancer):
        self.attributes = []
        self.attributes.append(int(age)) # 0
        self.attributes.append(int(sexp))
        self.attributes.append(int(num_pregnancies))
        self.attributes.append(int(smokes))
        self.attributes.append(int(ysmokes * packsperyear))
        self.attributes.append(int(hcon)) # 5
        self.attributes.append(int(hcon_years))
        self.attributes.append(int(iud))
        self.attributes.append(int(iud_years))
        self.attributes.append(int(std))
        self.attributes.append(int(std_num)) # 10
        self.attributes.append(int(condy))
        self.attributes.append(int(cerv_condy))
        self.attributes.append(int(vag_condy))
        self.attributes.append(int(vulvo_condy))
        self.attributes.append(int(syphilis)) # 15
        self.attributes.append(int(pelv))
        self.attributes.append(int(herp))
        self.attributes.append(int(molluscum))
        self.attributes.append(int(aids))
        self.attributes.append(int(hiv)) # 20
        self.attributes.append(int(hep_b))
        self.attributes.append(int(hpv))
        self.attributes.append(int(time_first))
        self.attributes.append(int(time_last))
        self.cancer = bool(cancer)


def guess_class(p, weights):
    num = 0
    for i in range(25):
        num += weights[i] * p.attributes[i]
    num += weights[25]
    if num > 0:
        return 1
    else:
        return 0


def adjust_weights(p, w, learn_rate, outcome):
    weights = w
    for i in range(25):
        if p.attributes[i] != -1:
            weights[i] = weights[i] + (learn_rate * outcome)
    weights[25] = weights[25] + (learn_rate * outcome)
    return weights


def epoch(parray, w, learn_rate):
    weights = w
    for p in parray:
        guess = guess_class(parray[p], weights)
        weights = adjust_weights(parray[p], weights, learn_rate, parray[p].cancer - guess)


def read_people():
    f = open("risk_factors_cervical_cancer.csv", "r")
    f.readline()
    parray = []
    for x in range(858):
        f1 = f.readline()
        fl = f1.split(",")
        for i in range(36):
            if fl[i] == "?":
                fl[i] = -1
        age = fl[0]
        sexp = float(fl[1])
        num_preg = float(fl[3])
        smokes = float(fl[4])
        smoke_years = float(fl[5])
        packs_year = float(fl[6])
        hcon = float(fl[7])
        hcon_years = float(fl[8])
        iud = float(fl[9])
        iud_years = float(fl[10])
        std = float(fl[11])
        std_num = float(fl[12])
        condy = float(fl[13])
        cerv_condy = float(fl[14])
        vag_condy = float(fl[15])
        vulvo_condy = float(fl[16])
        syphilis = float(fl[17])
        pelv = float(fl[18])
        herpes = float(fl[19])
        molluscum = float(fl[20])
        aids = float(fl[21])
        hiv = float(fl[22])
        hep_b = float(fl[23])
        hpv = float(fl[24])
        time_first = float(fl[26])
        time_last = float(fl[27])
        cancer = math.floor(float(fl[28]))

        p = Person(age, sexp, num_preg, smokes, smoke_years, packs_year, hcon, hcon_years, iud, iud_years, std, std_num,
                   condy, cerv_condy, vag_condy, vulvo_condy, syphilis, pelv, herpes, molluscum, aids, hiv, hep_b, hpv,
                   time_first, time_last, cancer)

        parray.append(p)

    f.close()
    return parray


parray = read_people()
count = 0
for x in range(858):
    p = parray[x]
    if p.cancer:
        count += 1
print(count)
