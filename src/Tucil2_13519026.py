# Nama  : Gde Anantha Priharsena
# NIM   : 13519026
# Kelas : K01

import os.path
class matkul:  
    def __init__(self, code, prereq):  
        self.code = code  
        self.prereq = prereq
        self.countPrereq = len(prereq)
        self.isPicked = False

def isAllPicked(listmatkul):
    i = 0
    isAllPick = True
    while (i<len(listmatkul) and isAllPick):
        if(not(listmatkul[i].isPicked)):
            isAllPick = False
        else:
            i+=1
    return isAllPick

def getAllZeroPrereqAndNotPicked(listmatkul):
    res = []
    for i in range(len(listmatkul)):
        if(listmatkul[i].countPrereq ==0 and not(listmatkul[i].isPicked)):
            res.append(listmatkul[i].code)
    return res

def removeMatkulFromPrereqOtherMatkul(matkul, listmatkul):
    for i in range(len(listmatkul)):
        if(matkul in listmatkul[i].prereq):
            listmatkul[i].countPrereq -= 1
        if(matkul == listmatkul[i].code):
            listmatkul[i].isPicked = True
    return listmatkul

def printKSM(ksm):
    for i in range(len(ksm)):
        if(i==0):
            print("Semester I : ", end="")
        elif(i==1):
            print("Semester II : ", end="")
        elif(i==2):
            print("Semester III : ", end="")
        elif(i==3):
            print("Semester IV : ", end="")
        elif(i==4):
            print("Semester V : ", end="")
        elif(i==5):
            print("Semester VI : ", end="")
        elif(i==6):
            print("Semester VII : ", end="")
        else:
            print("Semester VIII : ", end="")
        for j in range(len(ksm[i])):
            if(j == len(ksm[i])-1):
                print(ksm[i][j]+'.')
            else:
                print(ksm[i][j]+', ', end="")

# Pastikan file berada di folder test
filename = input("Masukkan Nama File: ")
d = os.path.dirname(os.getcwd())
f = open(d+"\\test\\"+filename, "r")

# creating list        
listMatkul = []  

for x in f:
    prereq = []
    x=x.rstrip(".\n")
    first_comma = x.find(',')
    if(first_comma == -1):
        code = x
        listMatkul.append(matkul(code,prereq))
    else:
        code = x[:first_comma]
        prereq=[pre.strip() for pre in x[first_comma+1:].split(',')]
        listMatkul.append(matkul(code,prereq))

ksm = []
semester = 1
while(semester <= 8 and not(isAllPicked(listMatkul))):
    thisSemester = getAllZeroPrereqAndNotPicked(listMatkul)
    for matkul in thisSemester:
        listMatkul = removeMatkulFromPrereqOtherMatkul(matkul, listMatkul)
    ksm.append(thisSemester)
    semester+=1

printKSM(ksm);
    