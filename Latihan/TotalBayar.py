#Total Pembayaran
#I.S. : Pengguna memasukan kode barang dan jumlah yang di beri (jumlah)
#F.s. : Menampilkan diskon, total bayar dan uang kembalian

KodeBarang = str(input("Masukan Kode Barang    : "))
JumlahBeli = int(input("Masukan Jumlah Beli    : "))
Diskon = int(input("Masukan Besaran Diskon : "))

#menentukan nama barang dan harga satuan
NamaBarang = "Pakaian"
HargaSatuan = 75000

if (KodeBarang == "TS02"):
    NamaBarang = "Tas"
    HargaSatuan = 65500

print("Kode Barang     : " , KodeBarang)
print("Nama Barang     : " , NamaBarang)
print("Harga Satuan : " , HargaSatuan)

#menentukan harga total
HargaTotal = HargaSatuan * JumlahBeli

print("Harga Total : ", HargaTotal)

#menentukan diskon
Diskon = 0

print(f"Diskon :", Diskon)

if (KodeBarang == "TS02" and JumlahBeli >= 10):
    Diskon = int(input("Masukan Besar Diskon : "))
    TotalDiskon = Diskon * 1 / 100
    Diskon = TotalDiskon * HargaTotal

print(f"Diskon :", Diskon)

#menghitung total bayar
TotalBayar = HargaTotal - Diskon

print("Total Bayar :", TotalBayar)

#memasukan uang pembayaran
UangBayar = int(input("Uang Bayar : "))

print("Uang Bayar :", UangBayar)

#mengecek uang pembayaran
if (UangBayar < TotalBayar):
    Kurang = TotalBayar - UangBayar

print("Kurang :", Kurang)

#pembayaran yang kurang
PembayaranKurang = int(input("Masukan Uang Bayar : "))

if (UangBayar + PembayaranKurang - TotalBayar):
    Kembalian = UangBayar + PembayaranKurang - TotalBayar

print("Kembalian :", Kembalian)






