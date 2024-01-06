#Program Validasi Tanggal
#I.S. : Pengguna memasukan tanggal,bulan dan tahun
#F.S. : Menampilkan Hasil validitas tanggal

#Memasukan tanggal, bulan, tahun
Tanggal = int(input("Tanggal : "))
Bulan = int(input("Bulan   : "))
Tahun = int(input("Tahun   : "))

#Proses menentukan validitas tanggal
if (Bulan == 2 and Tanggal <= 29):
    if (Tahun % 4 == 0):
        Hasil = "adalah tanggal valid"
    else:
        Hasil = "bukan tanggal valid"
else:
    if (Bulan <= 12):
        if (Bulan == 1 and Tanggal <= 31):
            Hasil = "adalah tanggal valid"
        elif (Bulan == 2 and Tanggal <= 28):
            Hasil = "adalah tanggal valid"
        elif (Bulan == 3 and Tanggal <= 31):
            Hasil = "adalah tanggal valid"
        elif (Bulan == 4 and Tanggal <= 30):
            Hasil = "adalah tanggal valid"
        elif (Bulan == 5 and Tanggal <= 31):
            Hasil = "adalah tanggal valid"
        elif (Bulan == 6 and Tanggal <= 30):
            Hasil = "adalah tanggal valid"
        elif (Bulan == 7 and Tanggal <= 31):
            Hasil = "adalah tanggal valid"
        elif (Bulan == 8 and Tanggal <= 31):
            Hasil = "adalah tanggal valid"
        elif (Bulan == 9 and Tanggal <= 30):
            HAsil = "adalah tanggal valid"
        elif (Bulan == 10 and Tanggal <= 31):
            Hasil = "adalah tanggal valid"
        elif (Bulan == 11 and Tanggal <= 30):
            HAsil = "adalah tanggal valid"
        elif (Bulan == 12 and Tanggal <= 31):
            Hasil = "adalah tanggal valid"
        else:
            Hasil = "bukan tanggal valid"
#Otput
print("Tanggal ",Tanggal,"/",Bulan,"/",Tahun," ",Hasil,sep="")