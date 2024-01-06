nilai = int(input("Masukan Nilai : "))

def Valiadasi (nilai):
    if(nilai // 2 == 0 ) :
        Hasil = print("Nilai Genap")
    else:
        Hasil = print("Nilai Ganjil")

    return Hasil
print(Valiadasi(nilai))