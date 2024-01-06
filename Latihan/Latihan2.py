# Biaya Rental Warnet
#I.S. Pengguna memasukan jam masuk, menit masuk, jam keluar, menit keluar
#F.S. Menampilkan hasil perhitungan biaya warnet

# Input
JamMasuk = int(input("Masukan Jam Masuk       : "))
MenitMasuk = int(input("Masukan Menit Masuk   : "))
JamKeluar = int(input("Masukan Jam Keluar     : "))
MenitKeluar = int(input("Masukan Menit Keluar : "))
print("-----------------------------------")

if JamKeluar < JamMasuk :
    JamKeluar = JamKeluar + 24

LamaRental = ((JamKeluar - JamMasuk) * 60) + ((MenitKeluar - MenitMasuk)
LamaRentalJam = LamaRental // 60
LamaRentalMenit = LamaRental % 60
print ("Lama Rental :", LamaRental,"menit","("Lamarentaljam,"jam")
