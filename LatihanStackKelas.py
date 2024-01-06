# Program Stack Mahasiswa
# I.S. Pengguna Memilih Menu Yang Ditampilkan
# F.S. Program Akan Menampilkan Hasil Pilihan Menu

MAKS_MHS = 20

Nim = []
Nama = []
Nilai = []
Indeks = []

# Funtion Kosong
def kosong(Top):
    if(Top == 0):
        return True
    else:
        return False

# Function Penuh
def penuh(Top):
    if(Top == MAKS_MHS):
        return True
    else:
        return False

# Procedure Untuk Memasukan Data Ke Stack Mahasiswa
def Push(Nim, Nama, Nilai, Indeks, Nim_baru, Nama_baru, Nilai_baru, Indeks_baru_):
    Top = len(Nim)
    if(not penuh(Top)):
        Nim.append(Nim_baru)
        Nama.append(Nama_baru)
        Nilai.append(Nilai_baru)
        Indeks.append(Indeks_baru_)
    else:
        print("Data Mahasiswa Sudah Penuh")

# Menampilkan Data stack Mahasiwa
def TampilDataStack(Nim, Nama, Nilai, Indeks):
    if(not kosong(Top)):
        print("         Isi Data Stack Mahasiswa        ")
        print("=========================================")
        i = 1
        while (i <= Top-1):
            print(i+1, " | ", Nim[i], " | ", Nama[i]," | ", Nilai[i], " | ", Indeks[i])
            i += 1

    else:
        print("Data Mahasiswa Kosong!")

# Function Indeks Mahasiswa
def NilaiIndeks(Nilai_baru) :
    if(Nilai_baru >= 80) and (Nilai_baru <= 100) :
        IndeksNilai = "A"
    elif(Nilai_baru >= 70) and (Nilai_baru <= 79) :
        IndeksNilai = "B"
    elif(Nilai_baru >= 60) and (Nilai_baru <= 69) :
        IndeksNilai = "C"
    elif(Nilai_baru >= 50) and (Nilai_baru <= 59) :
        IndeksNilai = "D"
    else :
        IndeksNilai = "E"

    return IndeksNilai

# Procedure Mengeluarkan Isi Stack Mahasiswa
def Pop(Nim, Nama, Nilai, Indeks):
    Top = len(Nim)
    if (not kosong(Top)):
        Nim.pop()
        Nama.pop()
        Nilai.pop()
        Indeks.pop()
    else:
        print("Data Mahasiswa Kosong!")

# Menampilkan Data stack Mahasiwa (Hasil POP)
def TampilDataPop(Nim, Nama, Nilai, Indeks) :
    Top = len(Nim)
    if(not kosong(Top)):
        print("         Isi Data Stack Mahasiswa        ")
        print("=========================================")
        No = 1
        while (not kosong(Top)):
            print(No, " | ", Nim[-1], " | ", Nama[-1]," | ", Nilai[-1], " | ", Indeks[-1])
            No += 1
            Pop(Nim, Nama, Nilai, Indeks)
            Top = len(Nim)
    else:
        print("Data Mahasiswa Kosong!")

# Program Utama
Top = len(Nim)
print("Menu Pilihan")
print("1. Isi Data Mahasiswa")
print("2. Tampil Data Mahasiswa")
print("0. Keluar")

menu = int(input("Masukan Menu : "))

while (menu != 0) :
    if (menu == 1) :
        if (not penuh(Top)) :
            Nim_baru = str(input("Nim : "))
            Nama_baru = str(input("Nama : "))
            Nilai_baru = int(input("Nilai : "))
            Indeks_baru = NilaiIndeks(Nilai_baru)
        print("Indeks : ", Indeks_baru)
        Push(Nim, Nama, Nilai, Indeks, Nim_baru, Nama_baru, Nilai_baru, Indeks_baru)
    elif (menu == 2) :
        TampilDataPop(Nim, Nama, Nilai, Indeks)
    else:
        print("Menu Salah")

    print("Menu Pilihan")
    print("1. Isi Data Mahasiswa")
    print("2. Tampil Data Mahasiswa")
    print("0. Keluar")

    menu = int(input("Masukan Menu : "))
