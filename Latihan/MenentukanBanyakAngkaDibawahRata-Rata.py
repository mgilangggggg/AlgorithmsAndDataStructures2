# I.S. : Linked list sudah terdefinisi
# F.S. : Menampilkan banyaknya angka yang dibawah rata-rata

print("Program Menghitung Nilai Rata-Rata")

n = int(input("\nBanyaknya Data: "))

print() #Membuat baris baru
data = []
jum = 0

for i in range(0, n):
    temp = int(input("Masukkan data ke-%d: " % (i+1)))
    data.append(temp)
    jum += data[i]
    rata2 = jum / n

print("\nJumlah Dibawah Rata - rata  = %0.2f" % rata2)