KodeBarang = str(input("Masukan Kode Barang : "))
JumlahBeli = int(input("Masukan Jumlah Beli : "))
Pakaian = 75000
Tas = 65500
Diskon = 0

if (KodeBarang == "TS02" and not JumlahBeli >= 10 ):
    NamaBarang = "Tas"
    HargaSatuan = Tas
    BesarDiskon = int(input("Masukan Besar Diskon : "))
    HargaTotal = Tas * JumlahBeli
    Diskon = HargaTotal * BesarDiskon / 100
    Harga = HargaTotal - Diskon

else:
    NamaBarang = "Tas"
    HargaSatuan = Tas
    HargaTotal = Tas * JumlahBeli
    Harga = HargaTotal

if (KodeBarang == "PK01"):
    HargaSatuan = Pakaian
    HargaTotal = Pakaian * JumlahBeli
    NamaBarang = "Pakaian"
    Harga = HargaTotal


print("Kode Barang  : ", KodeBarang)
print("Nama Barang  : ", NamaBarang)
print("Harga Satuan : ", HargaSatuan)
print("Harga Total  : ", HargaTotal)


if Diskon != 0  :
    print("Diskon   : ", Diskon)
    print("Total Bayar  : ", Harga)


UangBayar = int(input("Masukan Uang Pembayaran :"))
Kembalian = UangBayar - Harga
if(UangBayar > Harga):
    print("Uang Bayar : ", UangBayar)
    print("Kembalian  : ", Kembalian)
else:
    print("Uang Anda Kurang")