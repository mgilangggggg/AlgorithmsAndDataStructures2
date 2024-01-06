#Program_Keterangan_Lulus
#I.S. : Nilai diinputkan user, harus antara 0 s/d 100
#F.S. : Keterangan kelulusan ditampilkan

nilai = int(input("Masukan nilai : "))

while (nilai >= 0) and (nilai <= 100):
    if nilai >= 45:
        print("Lulus")
    else:
        print("Tidak Lulus")
