#Program Menukarkan Dua Angka
#I.S : Diberikan dua angka var angka1=5 dan var angka2=2
#F.S : Menampilkan angka yang sudah bertukar

#Angka1=5
#Angka2=2

Angka1 = int(input("Masukan Angka 1 : "))
Angka2 = int(input("Masukan Angka 2 : "))

print("Angka Sebelum Bertukar")
print("Angka 1 = ",Angka1)
print("Angka 2 = ",Angka2)

#proses Pertukaran
Angka1 = Angka1+Angka2
Angka2 = Angka1-Angka2
Angka1 = Angka1-Angka2

#Angka3=Angka1
#Angka1=Angka2
#Angka2=Angka3

print("Angka Setelah Bertukar")
print("Angka 1 = ",Angka1)
print("Angka 2 = ",Angka2)
