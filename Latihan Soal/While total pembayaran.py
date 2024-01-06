# Total_Pembayaran
# I.S. : pengguna memasukkan kode barang dan jumlah yang dibeli (Jumlah)
# F.S : menampilkan diskon, total bayar dan uang kembalian

# Daftar Kode barang,nama barang, harga satuan
print("-----------------------------------------------------")
print("| Kode Barang |      Nama Barang     | Harga Satuan | ")
print("-----------------------------------------------------")
print("|    PK01     |    Singkong Balado   | Rp. 10.000,- | ")
print("|    TS02     |    Singkong Keju     | Rp. 12.000,- | ")
print("|    TS03     |    Singkong Pedas    | Rp. 12.000,- | ")
print("|    TS04     |    Singkong Original | Rp. 10.000,- | ")
print("-----------------------------------------------------")


# Pengguna memasukkan kode barang dan jumlah barang
KodeBarang = str(input("Masukkan Kode Barang  : "))
Jumlah = int(input("Masukkan Jumlah Beli  : "))

# Menentukan nama barang dan harga satuan
NamaBarang = "Tas"
HargaSatuan = 65500

KodeBarang = KodeBarang.upper()
if (KodeBarang == "PK01"):
    NamaBarang = "Pakaian"
    HargaSatuan = 75000

# Menghitung harga total
HargaTotal = HargaSatuan * Jumlah

# Menentukan diskon
BesarDiskon = 0

if (KodeBarang == "TS02" and Jumlah >= 10):
    BesarDiskon = int(input("Besar Diskon (%)      : "))

Diskon = HargaTotal * BesarDiskon // 100

# Menghitung total bayar
TotalBayar = HargaTotal - Diskon

# Menampilkan Kode barang, nama barang, harga satuan, harga total, diskon, total bayar
print("Kode Barang           : ", KodeBarang, sep="")
print("Nama Barang           : ", NamaBarang, sep="")
print("Harga Satuan          : ", "Rp.", "%10d" % (HargaSatuan), ",-", sep="")
print("Harga Total           : ", "Rp.", "%10d" % (HargaTotal), ",-", sep="")
print("Diskon                : ", "Rp.", "%10d" % (Diskon), ",-", sep="")
print("Total Bayar           : ", "Rp.", "%10d" % (TotalBayar), ",-", sep="")

# Memasukkan uang pembayaran
Pembayaran = int(input("Uang Bayar            : Rp."))

# Pengulangan apabila Uang Bayar lebih kecil dari total bayar
while Pembayaran < TotalBayar:
    print("Maaf, Uang Bayar tidak mencukupi. Silahkan masukkan Uang Bayar sekali lagi.")
    Pembayaran = int(input("Uang Bayar            : "))

# Menghitung uang kembalian
Kembalian = Pembayaran - TotalBayar

# Menampilkan uang kembalian
print("Kembalian             : ", "Rp.", "%10d" % (Kembalian), ",-", sep="")
