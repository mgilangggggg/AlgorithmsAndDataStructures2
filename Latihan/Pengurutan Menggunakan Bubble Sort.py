NIM = []
Nama = []

i = 0
NIM.append(str(input(f"Masukkan NIM ke-{i + 1}: ")))

while (NIM[i] != "99999999"):
    Nama.append(str(input(f"Masukkan Nama Mahasiswa ke-{i + 1}: ")))
    i += 1
    NIM.append(str(input(f"Masukkan NIM ke-{i + 1}: ")))

NIM.pop()
N = len(NIM)

print("Menu Pengurutan")
print("-------------------")
print("1. Pengurutan NIM")
print("2. Pengurutan Nama")
print("0. Keluar")

Menu = int(input("Pilih Menu: "))

if (Menu < 0) or (Menu > 2):
    print("Menu tidak tersedia, Pilih Ulang!")
    Menu = int(input("Pilih Menu: "))


def UrutNIMAsc(NIM, Nama, N):
    for i in range(N):
        max = i
        for j in range(i + 1, N):
            if (NIM[max] > NIM[j]):
                max = j
            NIM[i], NIM[max] = NIM[max], NIM[i]
            Nama[i], Nama[max] = Nama[max], Nama[i]
    return NIM, Nama


def UrutNamaDsc(NIM, Nama, N):
    for i in range(N):
        for j in range(N - i - 1):
            if (Nama[j] < Nama[j + 1]):
                Nama[j], Nama[j + 1] = Nama[j + 1], Nama[j]
    return NIM, Nama


def TampilData(NIM, Nama):
    print()
    print()
    print()
    print("          Daftar Mahasiwa")
    print("------------------------------------")
    print("! NO !    NIM    ! Nama Mahasiswa  !")
    print("------------------------------------")
    for i in range(N):
        print("! %-2s ! " % (i + 1), "%-8s !" % NIM[i], "%-15s !" % Nama[i])
    print("------------------------------------")


while (Menu != 0):
    if (Menu == 1):
        UrutNIMAsc(NIM, Nama, N)
        TampilData(NIM, Nama)
    else:
        UrutNamaDsc(NIM, Nama, N)
        TampilData(NIM, Nama)

    print()
    print()
    print("Menu Pengurutan")
    print("-------------------")
    print("1. Pengurutan NIM")
    print("2. Pengurutan Nama")
    print("0. Keluar")

    Menu = int(input("Pilih Menu: "))

    if (Menu < 0) or (Menu > 2):
        print("Menu tidak tersedia, Pilih Ulang!")
        Menu = int(input("Pilih Menu: "))