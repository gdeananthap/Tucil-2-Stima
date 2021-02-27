# Nama  : Gde Anantha Priharsena
# NIM   : 13519026
# Kelas : K01

# Program SI-EKS
# Kamus
# Import library untuk membaca file masukan mata kuliah dan prerequisitesnya
import os.path

# Deklarasi class matkul dan constructornya
# matkul adalah singkatan dari mata kuliah
class matkul:  
    def __init__(self, code, prereq):  
        self.code = code  # Kode Matkul, string
        self.prereq = prereq # List of prerequisites, list of string
        self.countPrereq = len(prereq) # Banyaknya prerequisites yang belum diambil, integer
        self.isPicked = False # Status matkul, boolean

def isAllPicked(listmatkul):
    # Fungsi ini digunakan untuk mengecek apakah semua matkul yang ada di listmatkul sudah diambil semua
    # I.S. listmatkul terdefinisi sebagai list of object matkul
    # F.S. Jika semua matkul sudah diambil return True, jika tidak return False
    i = 0
    isAllPick = True
    # Iterasi selama belum ditemukan matkul yang belum diambil
    while (i<len(listmatkul) and isAllPick):
        if(not(listmatkul[i].isPicked)):
            isAllPick = False
        else:
            i+=1
    return isAllPick    

def getAllZeroPrereqAndNotPicked(listmatkul):
    # Fungsi ini digunakan untuk mendapatkan semua matkul yang bisa diambil (semua prerequisites sudah diambil) 
    # dan belum pernah diambil pada semester sebelumnya
    # I.S. listmatkul terdefinisi sebagai list of object matkul
    # F.S. mengembalikan list of string (list of kode matkul) dari matkul yang semua prerequisitesnya 
    # sudah diambil dan belum pernah diambil pada semester sebelumnya
    res = []
    for i in range(len(listmatkul)):
        if(listmatkul[i].countPrereq ==0 and not(listmatkul[i].isPicked)):
            # Jika prerequisites matkul sudah diambil semua dan matkul ini belum pernah diambil maka tambahkan ke list res
            res.append(listmatkul[i].code)
    return res

def removeMatkulFromPrereqOtherMatkul(matkul1, listmatkul):
    # Fungsi ini digunakan untuk mengurangi jumlah prerequisites yang belum diambil oleh setiap matkul pada 
    # listmatkul yang memiliki prerequisites matkul1
    # I.S. listmatkul terdefinisi sebagai list of object matkul, matkul1 adalah salah satu matkul pada listmatkul
    # F.S. Semua matkul yang memiliki matkul1 sebagai prerequisites akan berkurang countPrereq nya sebanyak 1
    for i in range(len(listmatkul)):
        if(matkul1 in listmatkul[i].prereq):
            # Jika matkul1 merupakan salah satu prereq dari suatu matkul pada listmatkul kurangi countPrereqnya sebanyak 1
            listmatkul[i].countPrereq -= 1
        if(matkul1 == listmatkul[i].code):
            # Ubah status matkul1 pada listmatkul menjadi sudah terambil, sehingga tidak bisa diambil lagi pada semester berikutnya
            listmatkul[i].isPicked = True
    return listmatkul

def printKSM(ksm, X):
    # Fungsi ini digunakan untuk menampilkan rencana kuliah seorang mahasiswa bernama X
    # I.S. ksm berisi list of (list of string(kode matkul)) dari semester 1-N dengan N maksimal 8
    # F.S. Rencana Studi ditampilkan pada layar
    print('\n------------------------------------------------------------------------------------------------------------------------')
    print('                                        '+X+' Course Plan                                                               ')
    print('------------------------------------------------------------------------------------------------------------------------')
    for i in range(len(ksm)):
        # Cek apakah ada matkul yang diambil pada semester ke-i
        if(len(ksm[i]) > 0):
            # Print semester ke i
            if(i==0):
                print("Semester I    : ", end="")
            elif(i==1):
                print("Semester II   : ", end="")
            elif(i==2):
                print("Semester III  : ", end="")
            elif(i==3):
                print("Semester IV   : ", end="")
            elif(i==4):
                print("Semester V    : ", end="")
            elif(i==5):
                print("Semester VI   : ", end="")
            elif(i==6):
                print("Semester VII  : ", end="")
            else:
                print("Semester VIII : ", end="")
            for j in range(len(ksm[i])):
                # Print kode matkul pada semester ke i
                if(j == len(ksm[i])-1):
                    print(ksm[i][j]+'.')
                else:
                    print(ksm[i][j]+', ', end="")

def bootlogo():
    # Menampilkan boot logo aplikasi pada layar
    print('                                                    ,---,_          ,                                               ')       
    print('                                                     _>   ''-.  .--  /                                              ')      
    print('                                                .--''` ._     `//   <_                                              ') 
    print('                                                 >,-` ._`.. ..__ . ' '-.                                            ')   
    print('                                              .-`   .``         ``.     `.                                          ')    
    print('                                               >   / >`-.     .- < \ , `._\                                         ')     
    print('                                              /    ;  -._>   <_.-`  ;  `._>                                         ')    
    print('                                              `>  ,/  /___\ /___\  \_  /                                            ')        
    print('                                              `.-|(|  \o_/  \o_/   |)|`                                             ')   
    print('                                                  \;        \      ;/                                               ')    
    print('                                                    \  .-,   )-.  /                                                 ')    
    print('                                                     /`  .`-`.  `\                                                  ')      
    print('                                                    ;_.-`.___. -.;                                                  ')   
    print('                                _____    ____                         ______    __ __   _____                       ')
    print('                               / ___/   /  _/                        / ____/   / //_/  / ___/                       ')
    print('                               \__ \    / /          ______         / __/     / ,<     \__ \                        ')
    print('                              ___/ /  _/ /          /_____/        / /___    / /| |   ___/ /                        ')
    print('                             /____/  /___/                        /_____/   /_/ |_|  /____/                         ')
    print('\n                                       Your Personal Course Enrollment Planner                                   \n')
                                                                


# Algoritma Program Utama

#Tampilkan Boot Logo
bootlogo()

# Membaca nama mahasiswa dan file mata kuliah dengan prerequisitesnya dalam format yang sudah ditentukan
# Pastikan file berada di folder test dan format sesuai
name = input("Enter Your Name   : ")
filename = input("Enter Course File : ")
d = os.path.dirname(os.getcwd())
f = open(d+"\\test\\"+filename, "r")

# Inisialisasi list of object matkul        
listMatkul = []  

# Baca setiap matkul dan prerequisitesnya pada file per baris
for x in f:
    # Inisialisasi list kosong untuk prerequisites matkul untuk menghindari kasus prerequisites matkul 
    # pada baris sebelumnya yang lebih banyak sehinggra prerequisites tidak sesuai dengan file  
    prereq = []
    # Untuk setiap baris hilangkan karakter . dan newline pada akhir baris
    x=x.rstrip(".\n")
    # Dapatkan index pertama dari koma untuk memisahkan matkul dengan prerequisitesnya
    first_comma = x.find(',')
    if(first_comma == -1):
        # Jika tidak ditemukan koma, maka matkul tidak memiliki prerequisites
        code = x
        # Construct class matkul dengan kode matkul dan prereq berupa list kosong karena matkul ini 
        # tidak memiliki prereq. Kemudian tambahkan kedalam list of object matkul
        listMatkul.append(matkul(code,prereq))
    else:
        # Ambil kode matkul dari matkul sebelum koma pertama
        code = x[:first_comma]
        # Untuk setiap kode matkul setelah koma pertama, lakukan split string 
        # dengan parameter koma sebagai pemisahnya, kemudian hilangkan whitespace
        prereq=[pre.strip() for pre in x[first_comma+1:].split(',')]
        # Construct class matkul dengan kode matkul dan prereqnya. 
        # Kemudian tambahkan kedalam list of object matkul
        listMatkul.append(matkul(code,prereq))

# Inisialisasi list of list nama matkul pada setiap semester dan semester dimulai dari semester 1
ksm = []
semester = 1
# Iterasi selama semester masih valid (1<=semester<=8) dan semua matkul yang tersedia belum terambil
# Sehingga jika matkul masih tersisa tapi semester sudah mencapai 8 atau semua matkul sudah terambil
# maka iterasi akan berhenti
while(semester <= 8 and not(isAllPicked(listMatkul))):
    # Gunakan pendekatan Topological Sort 
    # Manfaatkan Algoritma Decrease and Conquer
    # Ambil semua mata kuliah yang dapat diambil pada semester ini dengan fungsi getAllZeropPrereqAndNotPicked
    thisSemester = getAllZeroPrereqAndNotPicked(listMatkul)
    # Untuk setiap matkul yang dapat diambil pada semester ini
    for matkul in thisSemester:
        # Kurangi countPrereq sebanyak 1 untuk setiap mata kuliah yang memiliki matkul sebagai prerequisites 
        listMatkul = removeMatkulFromPrereqOtherMatkul(matkul, listMatkul)
    # Tambahkan mata kuliah yang dapat diambil pada semester ini ke list ksm dan lanjutkan iterasi
    ksm.append(thisSemester)
    semester+=1

# Print Hasil Rencana Studi Mahasiswa dengan pendekatan topological sort dan memanfaatkan decrease and conquer
printKSM(ksm, name)

# Close file
f.close()