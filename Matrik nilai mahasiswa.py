# Program Matriks Nilai Mahsiswa
# I.S : Masukan jumlah mahasiswa,matakuliah, nim, nilai per matakuliah per mahasiswa
# F.s : menampilkan nilai dan indeks prestasi

# array 1 dimensi untuk Nim, MataKuliah, Dan SKS
nim_mhs = []
matkul = []
sks = []

# arrray 2 dimensi untuk nilai
matriks_nilai = []

byk_mhs = int(input("Masukan Banyak Mahasiswa : "))
byk_matkul = int(input("Masukan Banyak Mata kuliah : "))


def IsiArray(byk_mhs, byk_matkul, nim_mhs, matkul, sks, matriks_nilai):
    for i in range(byk_matkul):
        print("Masukan Nama mata kuliah ke-", i+1, ":", end=" ")
        nama_matkul = str(input(" "))
        print("Masukan nanyak sks untuk  mata kuliah ke-",
              nama_matkul, ":", end=" ")
        banyak_sks = str(input(" "))
        matkul.append(nama_matkul)
        sks.append(banyak_sks)

    for i in range(byk_mhs):
        print("Masukan NIM MAhasiswa ke-", i + 1, ":", end=" ")
        nim = str(input(" "))
        nim_mhs.append(nim)
        sementara = []
        for j in range(byk_matkul):
            print("Masukan nilai", matkul[j], ":", end=" ")
            nilai = int(input(" "))
            sementara.append(nilai)
        print()
        matriks_nilai.append(sementara)


def Indeks_Prestasi(nilai):
    if (nilai > 79) and (nilai < 101):
        indek = "A"
    elif (nilai > 69) and (nilai < 80):
        indek = "B"
    elif (nilai > 59) and (nilai < 70):
        indek = "C"
    elif (nilai > 39) and (nilai < 60):
        indek = "D"
    else:
        indek = "E"
    return indek


def TampilMatrik_Nilai(nim_mhs, matkul, matriks_nilai):
    for i in range(0, len(matriks_nilai)):
        print("NIM MAhasiswa :", nim_mhs[i],)
        total_nilai = 0
        jumlah_sks = 0
        for j in range(0, len(matriks_nilai[0])):
            print("nilai", matkul[j], ":", matriks_nilai[i][j],
                  "(", Indeks_Prestasi(matriks_nilai[i][j]), ")")
            nilai_X_indeks = Indeks_Prestasi(
                Indeks_Prestasi(matriks_nilai[i][j])) * sks[j]
            total_nilai += nilai_X_indeks
            jumlah_sks += sks[j]
        Nilai_IP = total_nilai / jumlah_sks
        print("IP : ", Nilai_IP)
        print()


IsiArray(byk_mhs, byk_matkul, nim_mhs, matkul, sks, matriks_nilai)
TampilMatrik_Nilai(nim_mhs, matkul, matriks_nilai)
