#kalkulator_Fungsi
#{I.S. : Pengguna memasukan dua operand dan satu operator}
#{F.S. : Menampilkan hasil perhitungan dari kalkulator sederhana}

Opr1 = float(input("Masukan operator1 : "))
Opr2 = float(input("Masukan operator2 : "))
Operator = str(input("Operator : "))

while(Operator != "+") and (Operator != "-") and (Operator !=  "/") and (Operator != "*"):
    print("Opera2tor yang anda pilih tidak tersedia")
    Operator = str(input("Operator : "))

def TampilHasil(Opr1,Opr2,Operator):
    if(Operator == "+"):
        Hasil = Opr1 + Opr2
    elif(Operator == "-"):
        Hasil = Opr1 - Opr2
    elif(Operator == "/"):
        Hasil = Opr1 / Opr2
    elif(Operator == "*"):
        Hasil = Opr1 * Opr2
    else:
        print("masukan operator anda tidak ada")

    return Hasil

print(TampilHasil(Opr1,Opr2,Operator))
