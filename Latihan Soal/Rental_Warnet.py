#Rental_Warnet
#I.S. Pengguna memasukkan jam, menit masuk dan jam, menit keluar
#F.S. Program menampilkan lama rental dan biaya rental

#input
jam_masuk = int(input("Jam Masuk    : "))
menit_masuk = int(input("Menit Masuk  : "))
jam_keluar = int(input("Jam keluar   : "))
menit_keluar = int(input("Menit keluar : "))

#Proses
total_menit_masuk = jam_masuk * 60 + menit_masuk
total_menit_keluar = jam_keluar * 60 + menit_keluar

if total_menit_keluar >= total_menit_masuk :
    selang_menit = total_menit_keluar - total_menit_masuk
else :
    selang_menit = ((24 * 60) - total_menit_masuk) + total_menit_keluar

durasi_jam = selang_menit // 60
durasi_menit = selang_menit % 60

biaya_rental = (5000 * durasi_jam) + ((5000 / 60) * durasi_menit)

#Output
print("----------------------------------")
print("Lama Rental  : ", durasi_menit , "(",durasi_jam,"jam",durasi_menit,"menit",")")
print("Biaya Rental : ","Rp. ",int(biaya_rental))