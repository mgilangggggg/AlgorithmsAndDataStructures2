#ProgramTarifPemasanganListrik
#I.S. : Pengguna memasukan nama, alamat,jenis pelanggan sambungan (watt)
#F.S. : Menampilkan total tarif pemasangan listrik

#Memasukan nama,alamat,dan jenis
Nama = str(input("Masukan Nama Anda      : "))
Alamat = str(input("Masukan Alamat Anda    : "))
Jenis = str(input("Masukan Jenis Pelanggan : ")).lower

if (Jenis != "RUMAH TANGGA") and ( Jenis != "INDUSTRI") :
    print("Jenis Pelanggan",Jenis,"Tidak Ada !")
else :
    Watt = int(input("Masukkan Besaran Watt    : "))
    if (Jenis == "RUMAH TANGGA"):
        if Watt >= 2201 and Watt <= 4400 :
            Tarif = 1750000
        elif Watt >= 1201 and Watt <= 2200 :
            Tarif = 1500000
        elif Watt >= 901 and Watt <= 1200 :
            Tarif = 1200000
        elif Watt >= 451 and Watt <= 900 :
            Tarif = 850000
        else :
            Tarif = 650000
    else:
        print("Jumlah watt yang anda masukan tidak ada")
        if Watt >= 22001:
            Tarif = 6750000
        elif Watt >= 16001 and Watt <= 22000 :
            Tarif = 4500000
        elif Watt >= 12001 and Watt <= 16000 :
            Tarif = 3250000
        elif Watt >= 9501 and Watt <= 12000 :
            Tarif = 2750000
        else :
            Tarif = 2250000

    # Menghitung PPN
    Ppn = 0.1 * Tarif

    # Menghitung Biaya Administrasi
    Administrasi = 0.05 * Tarif

    TotalBiaya = Tarif + Ppn + Administrasi

    print("---------------------------------------")
    print("Nama Pelanggan     : ",Nama)
    print("Alamat Pelanggan   : ",Alamat)
    print("Jenis Pelanggan    : ",Jenis)
    print("Besaran Watt       : ",Watt,"watt")
    print("-------------------------------------- ")
    print("Biaya PPN          : Rp.","{:.2f}".format(Ppn),",-")
    print("Total Administrasi : Rp.","{:.2f}".format(Administrasi),",-")
    print("Total Biaya        : Rp.","{:.2f}".format(TotalBiaya),",-")