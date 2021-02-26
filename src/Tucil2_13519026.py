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
   
# Pastikan file berada di folder test
filename = input("Masukkan Nama File: ")
d = os.path.dirname(os.getcwd())
f = open(d+"\\test\\"+filename, "r")

# creating list        
listMatkul = []  

for x in f:
    code = ""
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


for matkul in listMatkul: 
    print( matkul.code, matkul.prereq, matkul.countPrereq, matkul.isPicked ) 
