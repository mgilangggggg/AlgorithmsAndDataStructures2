#Program Pengoahan Array Angka
# I.S Pengguna Memilih Menu
# F.S Program Menampilkan Pilihan Menu

Maks_Angka = 10
Angka = []

def IsiDataAngka(Angka,BanyakData):
    for i in range(BanyakData):
        DataBaru = int(input("Masukkan Sebuah Angka : "))
        Angka.append(DataBaru)

def RataAngka(Angka,BanyakData):
    Total = 0
    for i in range(BanyakData):
        Total = Total + Angka[i]

    return Total/BanyakData

def Tertinggi(Angka,BanyakData):
    Maks = Angka[0]
    for i in range(1,BanyakData):
        if(Angka[i] >= Maks):
            Maks = Angka[i]
    return Maks

def Terendah(Angka,BanyakData):
    Min = Angka[0]
    for i in range(1,BanyakData):
        if(Angka[i] < Min):
            Min = Angka[i]
    return Min

def TampilRata(Angka,BanyakData):
    print("Rata-Rata Angka : ",RataAngka(Angka,BanyakData))

def TampilTertinggiTerendah(Angka,BanyakData):
    print("Angka  Tertinggi : ",Tertinggi(Angka,BanyakData))
    print("Angka  Terendah  : ",Terendah(Angka, BanyakData))

def TambahAngka(Angka,BanyakData,AngkaBaru):
    if (BanyakData < Maks_Angka):
        BanyakData = BanyakData +1
        Angka.append(AngkaBaru)
    else:
        print("Data Sudah Penuh")

def SisipAngka(Angka,BanyakData,Posisisisip,AngkaBaru):
    if (BanyakData < Maks_Angka):
        if (Posisisisip >= 1) and (Posisisisip <= BanyakData):
            Angka.insert(Posisisisip,AngkaBaru)
            BanyakData = BanyakData+1
        else:
            print("Posisi Sisip Tidak Valid")
    else:
        print("Data Sudah Penuh")

def TampilAngka(Angka,BanyakData):
    for i in range(BanyakData):
        print('Data ke',i+1,":",Angka[i])
    #Tanpa Menampilkan Index Array
    #for i in Angka:
    #    print(i)

print("Menu Pilihan")
print("-"*30)
print("1. Isi Data Angka")
print("2. Rata Rata Angka")
print("3. Angka Tertinggi dan Terendah")
print("4. Penambahan Data Angka")
print("5. Penyisipan Data Angka")
print("6. Tampil Data Angka")
print("0. keluar")
menu = int(input("Masukkan Pilihan Menu : "))

while (menu != 0):
    if (menu == 1):
        BanyakData = int(input("Masukkan Jumlah Element : "))
        IsiDataAngka(Angka,BanyakData)
    elif (menu == 2):
        BanyakData= len(Angka)
        if (BanyakData == 0):
            print("Isi Data Angka Terlebih Dahulu ( Menu No 1 )")
        else:
            TampilRata(Angka,BanyakData)
    elif (menu == 3):
        BanyakData = len(Angka)
        if (BanyakData == 0):
            print("Isi Data Angka Terlebih Dahulu ( Menu No 1 )")
        else:
            TampilTertinggiTerendah(Angka,BanyakData)
    elif (menu == 4):
        BanyakData = len(Angka)
        if (BanyakData == 0):
            print("Isi Data Angka Terlebih Dahulu ( Menu No 1 )")
        else:
            AngkaBaru = float(input("Angka Yang Akan Ditambahkan : "))
            TambahAngka(Angka,BanyakData,AngkaBaru)
    elif (menu == 5):
        BanyakData = len(Angka)
        if (BanyakData == 0):
            print("Isi Data Angka Terlebih Dahulu ( Menu No 1 )")
        else:
            AngkaBaru = float(input("Angka Yang Akan Ditambahkan : "))
            Posisisisip = int(input("Posisi Yang Akan Disisipkan : "))
            SisipAngka(Angka,BanyakData,Posisisisip-1,AngkaBaru)
    else:
        BanyakData = len(Angka)
        if (BanyakData == 0):
            print("Isi Data Angka Terlebih Dahulu ( Menu No 1 )")
        else:
            TampilAngka(Angka,BanyakData)

    print("Menu Pilihan")
    print("-"*30)
    print("1. Isi Data Angka")
    print("2. Rata Rata Angka")
    print("3. Angka Tertinggi dan Terendah")
    print("4. Penambahan Data Angka")
    print("5. Penyisipan Data Angka")
    print("6. Tampil Data Angka")
    print("0. keluar")
    menu = int(input("Masukkan Pilihan Menu : "))