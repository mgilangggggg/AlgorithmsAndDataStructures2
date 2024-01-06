#Program penjumlahan 2 matriks
#I.S. pengguna memasukan banyakanya baris (n) dan banyaknya kolom (m) dan elemen
#F.S. program menampilkan matriks hasil penjumlahan berordo nxm

MAKSBARIS = 10
MAKSKKOLOM = 15

A = []
B = []
C = []

m = int(input('Masukan Jumlah Baris : '))
#validasi n
while(m < 1) or (m > MAKSBARIS):
    print(f"jumlah baris harus antara 1-{MAKSBARIS}. Ulangi")
    m = int(input("Masukan Jumlah Baris : "))

# n = int(input('Masukan Jumlah Kolom : '))
# validasi m
# while(n < 1) or (n > MAKSKOLOM):
#     print(f"jumlah kolom harus antara 1-{MAKSKOLOM}. Ulangi")
#     n = int(input("Masukan Jumlah Kolom : "))

def Isi2Matriks (A,B) :
    print('Masukan Maatriks A')
    for i in range(m) :
        A_sementara = []
        for j in range(n) :
            print('Masukan Data ke [',i,',',j,'] : ',end='')
            data_baru = int(input(''))
            A_sementara.append(data_baru)
        A.append(A_sementara)
    print()
    print('Masukan Maatriks B')
    for i in range(m) :
        B_sementara = []
        for j in range(n):
            print('Masukan Data ke [',i,',',j,'] : ',end='')
            data_baru = int(input(''))
            B_sementara.append(data_baru)
        B.append(B_sementara)

def JumlahAB(m,n,A,B):
    for i in range(m):
        Jumlah_sementara = []
        for j in range(n):
            Jumlah = A[i][j] + B[i][j]
            Jumlah_sementara.append(Jumlah)
        C.append(Jumlah_sementara)
    return C

def TampilMatriks(A,B) :
    print('Menampilkan Matriks A')
    for i in range(m) :
        for j in  range(n) :
            print(A[i][j],end=' ')
        print()

    print()
    print('Menampilkan Matriks B')
    for i in range(m) :
        for j in range(n) :
            print(B[i][j],end=' ')
        print()

    print()
    print('Menampilkan Matriks Hasil : ')
    C = JumlahAB(m,n,A,B)
    for i in range(m):
        for j in range(n):
            print(C[i][j], end=' ')
        print()

Isi2Matriks(A,B)
TampilMatriks(A,B)

Isi2Matriks(A,B)
print(A,end=' ')
print()
print(B,end=' ')