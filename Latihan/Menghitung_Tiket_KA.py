#Program Menghitung_Tiket_KA
#I.S. : Pengguna memilih jurusan dan memasukan banyak tiket
#F.S. : Menampilkan harga tiket dan total bayar

print("Perhitungan Tiket Kereta Api")
print("Jurusan Yang Tersedia :")
print("1. Jakarta")
print("2. Yogyakarta")
print("3. Surabaya")
print("-" * 30)

#Input
jurusan = int(input("Masukan Jurusan      : "))
banyak_tiket = int(input("Masukan Banyak Tiket : "))

print("-" * 30)
print()

#Proses
if  (jurusan==1) :
    harga_tiket = 150000
elif (jurusan==2) :
    harga_tiket = 300000
elif (jurusan==3) :
    harga_tiket = 400000
else :
    print("Jurusan Tidak Ada")

total_bayar = harga_tiket * banyak_tiket

#Output
print("Harga Tiket : Rp.",harga_tiket)
print("Banyak Tiket : Rp.",banyak_tiket)
print("Total Bayar : Rp.",total_bayar)