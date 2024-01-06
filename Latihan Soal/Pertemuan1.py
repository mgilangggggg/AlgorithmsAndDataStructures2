#Program Matriks Nilai
#I.S. Pengguna memasukan nim, mata kuliah, nilai per matakuliah per siswa
#F.S. Program menampilkan nilai dan indeks prestasi / IP

#Array 1 Dimensi untuk nim, mata kuliah, sks
from operator import index
from re import I
from textwrap import indent


nim_mhs = []
matkul = []
sks = []

#Array 2 Dimensi untuk nilai
matriks_nilai = []

byk_mhs = int(input('Masukan Banyak Mahasiswa   : '))
byk_matkul = int(input('Masukan Banyak Mata Kuliah : '))

def IsiArray (byk_mhs,byk_matkul,nim_mhs,matkul,sks,matriks_nilai) :
    for i in range (byk_matkul) :
        print('Masukan Nama Mata Kuliah Ke-',i+1,':',end=' ')
        nama_matkul = str(input(' '))
        print('Masukan Nama SKS untuk matkul-',nama_matkul,':',end=' ')
        Banyak_SKS = int(input(' '))
        matkul.append(nama_matkul)
        sks.append(Banyak_SKS)

    for i in range(byk_mhs) :
        print('Masukan NIM Mahasiswa Ke-',i+1,':',end=' ')
        nim = str(input(' '))
        nim_mhs.append(nim)
        sementara=[]
        for j in range(byk_matkul) :
            print('Masukan Nilai',matkul[j],':',end=' ')
            nilai = str(input(' '))
            sementara.append(nilai)
        print()
        matriks_nilai.append(sementara)

def Indeks_Prestasi (nilai) :
    if (nilai>79) and (nilai<100) :
        indeks='A'

    elif (nilai>69) and (nilai<80) :
        indeks='B'

    elif (nilai>59) and (nilai<70) :
        indeks='C'
    elif (nilai>39) and (nilai<60) :
        indeks='D'
    else:
        indeks='E'
    return indeks

def TampilMatrikNilai (nim_mhs,matkul,matriks_nilai) :
    for i in range(0, len(matriks_nilai)) :
        print('NIM Mahasiswa : ',nim_mhs[i])
        Total_Nilai = 0
        Jumlah_SKS = 0
        for j in range(0, len(matriks_nilai[0])) :

print('nilai',matkul[j], ':', matriks_nilai[i] [j], ('Indeks_Prestasi(matriks_nilai[i] [j]),')
        nilai_X_indeks = Indeks_Prestasi(Indeks_Prestasi(matriks_nilai[i][j])) * sks[j]
        Total_Nilai += nilai_X_indeks
        Jumlah_SKS += sks[j]
    Nilai_IP = Total_Nilai / Jumlah_SKS
    print("IP : ",Nilai_IP)
    print()


IsiArray(byk_mhs,byk_matkul,nim_mhs,matkul,sks,matriks_nilai)
TampilMatrik_Nilai(nim_mhs,matkul,matriks_nilai)