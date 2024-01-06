#Program Faktorial Rekursif
#I.S. : Pengguna memasukan nilai N
#F.S. : Menampilkan Faktorial Dari N

N = int(input("Masukan Nilai N : "))

def Faktorial (N) :
    #I.S. Nilai N Sudah Terdefinisi
    #F.S. Menghasilkan fungsi faktorial dari N
    if(N == 0) or (N == 1) :
        return 1
    else:
        return N * Faktorial(N-1)

def Tampil(N) :
    for i in range(N+1) :
        print("Nilai Faktorial", N )
#    print("Nilai Faktorial ",N, "Adalah", Faktorial(N))

Tampil(N)