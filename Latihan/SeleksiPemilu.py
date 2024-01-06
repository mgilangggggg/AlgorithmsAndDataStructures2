#Program Seleksi Pemilu
#I.S. : Pengguna memasukan umur dan status Pernikahan
#F.S. : Menampilkan boleh memilih atau tidak

Umur = int(input("Masukan Umur Anda : "))

if (Umur < 17):
    Menikah = input("Menikah Y/T : ")
    if (Menikah == "Y"):
        print("Anda boleh ikut pemilu")
    else:
        print("Anda belum boleh ikut pemilu")
else:
    print("Anda boleh ikut pemilu")