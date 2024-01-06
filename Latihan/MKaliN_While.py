M = int(input("Masukkan nilai M: "))

while (M < 0) or (M > 20):
    print("Harga M harus diantara 0 - 20, Ulangi!")
    M = int(input("Masukkan nilai M: "))

N = int(input("Masukkan nilai N: "))

while (N < 0) or (N > 20):
    print("Harga N harus diantara 0 - 15, Ulangi!")
    N = int(input("Masukkan nilai N: "))

if (M == 0) or (N == 0):
    HasilKali = 0
elif (M == 1):
    HasilKali = N
else:

    # While
    #HasilKali = N
    #i = 2
    #while (i <= M):
        #print(N)
        #if (i < M):
            #print("+")

        #HasilKali += N
        #i += 1

    # For
    # HasilKali = 0
    # for i in range(M):
    #   HasilKali += N

print("Hasil Perkalian %d dan %d =" % (M, N), HasilKali)