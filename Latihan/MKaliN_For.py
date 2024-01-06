#MKaliN_For
#I.S. : pengguna memasukan nilai M dan harga N
#F.S. : menampilkan hasil M x N menggunakan operator penjumlahan

M = int(input("Masukan Nilai M : "))
while (M < 0) or (M > 20):
    print("Nilai M harus antara 0 - 20, ulangi")
    M = int(input("Masukan Nilai M : "))

N = int(input("Masukan Nilai N : "))
while (N < 0) or (N > 10):
    print("Nilai N harus antara 0 - 15, ulangi")
    N = int(input("Masukan Nilai N : "))

if (M == 0) or (N == 0):
    HasilKali = N
elif (N == 1):
    HasilKali = M
elif (N == 1):
    HasilKali = N
    for i in range(2,M):
        HasilKali = HasilKali + n

print("Hasil :",HasilKali)