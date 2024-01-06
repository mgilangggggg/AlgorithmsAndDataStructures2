#Program Menghitung Komisi
#I.S. : Pengguna memasukan nama dan nilai penjualan
#F.S. : Program menampilkan nama dan komisi yang diperoleh

#Input
nama = str(input("Masukan Nama Salesman : "))
penjualan = float(input("Masukan Nilai Penjualan : "))

#Proses
komisi = 0.05 * penjualan

#Output
print("Nama Salesman : ",nama)
print("Besar Komisi : Rp. ",komisi)
print("Besar Komisi Terformat : Rp. ","{:.2f}".format(komisi))
