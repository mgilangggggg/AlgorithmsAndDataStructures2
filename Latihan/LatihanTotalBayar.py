#Program Total Bayar
#I.S. Pengguna memasukan  kode barang dan jumlah
#F.S. Menampilkan harga total, diskon, total bayar, dan

KodeBarang = str(input("Masukan Kode Barang : "))
Jumlah = int(input("Masukan Jumlah barang : "))

NamaBarang = "Tas"
HargaSatuan = 65500

KodeBarang = KodeBarang.upper()
if (KodeBarang == "PK01") :
    NamaBarang = "Pakaian"
    HargaSatuan = 75000

HargaTotal = HargaSatuan * Jumlah


Diskon = 0
if (KodeBarang == TS02 ) and (Jumlah >= 10) :
    BesarDiskon

TotalBayar = HargaTotal - Diskon

#menampilkan diskon dan total bayar
Pembayaran =
